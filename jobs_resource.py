from flask import jsonify
from flask_restful import abort, Resource
from data.jobs import Jobs
from data import db_session
from parse_job import parser


def job_not_found(job_id):
    session = db_session.create_session()
    job = session.query(Jobs).get(job_id)
    if not job:
        abort(404, message=f"Job {job_id} not found")


class JobsResource(Resource):
    def get(self, job_id):
        job_not_found(job_id)
        session = db_session.create_session()
        job = session.query(Jobs).get(job_id)
        return jsonify({'job': job.to_dict(
            only=('id', 'team_leader', 'job',
                  'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished'))})

    def put(self, job_id):
        args = parser.parse_args()
        job_not_found(job_id)
        session = db_session.create_session()
        job = {
            'team_leader': args['team_leader'],
            'job': args['job'],
            'work_size': args['work_size'],
            'collaborators': args['collaborators'],
            'start_date': args['start_date'],
            'end_date': args['end_date'],
            'is_finished': args['is_finished']
        }
        session.query(Jobs).filter(Jobs.id == job_id).update(job)
        session.commit()
        return jsonify({'success': 'OK'})

    def delete(self, job_id):
        job_not_found(job_id)
        session = db_session.create_session()
        job = session.query(Jobs).get(job_id)
        session.delete(job)
        session.commit()
        return jsonify({'success': 'OK'})


class JobsListResource(Resource):
    def get(self):
        session = db_session.create_session()
        jobs = session.query(Jobs).all()
        return jsonify({'jobs': [item.to_dict(
            only=('id', 'team_leader', 'job',
                  'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished')) for item in jobs]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        job = Jobs(
            team_leader = args['team_leader'],
            job = args['job'],
            work_size = args['work_size'],
            collaborators = args['collaborators'],
            start_date = args['start_date'],
            end_date = args['end_date'],
            is_finished = args['is_finished']
        )
        session.add(job)
        session.commit()
        return jsonify({'success': 'OK'})