from flask import jsonify
from flask_restful import abort, Resource
from data.users import User
from data import db_session
from parse_user import parser


def user_not_found(user_id):
    session = db_session.create_session()
    user = session.query(User).get(user_id)
    if not user:
        abort(404, message=f"News {user_id} not found")


class UsersResource(Resource):
    def get(self, user_id):
        user_not_found(user_id)
        session = db_session.create_session()
        user = session.query(User).get(user_id)
        return jsonify({'user': user.to_dict(
            only=('surname', 'name', 'age', 'position', 'speciality', 'address', 'email'))})

    def put(self, user_id):
        args = parser.parse_args()
        user_not_found(user_id)
        session = db_session.create_session()
        user = {
            'surname': args['surname'],
            'name': args['name'],
            'age': args['age'],
            'position': args['position'],
            'speciality': args['speciality'],
            'address': args['address'],
            'email': args['email']
        }
        session.query(User).filter(User.id == user_id).update(user)
        session.commit()
        return jsonify({'success': 'OK'})

    def delete(self, user_id):
        user_not_found(user_id)
        session = db_session.create_session()
        user = session.query(User).get(user_id)
        session.delete(user)
        session.commit()
        return jsonify({'success': 'OK'})


class UsersListResource(Resource):
    def get(self):
        session = db_session.create_session()
        users = session.query(User).all()
        return jsonify({'users': [item.to_dict(
            only=('surname', 'name', 'age', 'position', 'speciality', 'address', 'email')) for item in users]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        user = User(
            surname = args['surname'],
            name = args['name'],
            age = args['age'],
            position = args['position'],
            speciality = args['speciality'],
            address = args['address'],
            email = args['email']
        )
        session.add(user)
        session.commit()
        return jsonify({'success': 'OK'})