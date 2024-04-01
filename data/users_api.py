import flask
from flask import jsonify, make_response, request
from . import db_session
from .users import User


blueprint = flask.Blueprint(
    'users_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/users')
def get_users():
    db_sess = db_session.create_session()
    users = db_sess.query(User).all()
    return jsonify(
        {
            'users':
                [item.to_dict(only=('id', 'surname', 'name', 'age', 'position', 'speciality', 'address', 'email',
                                    'hashed_password', 'modified_date'))
                 for item in users]
        }
    )


@blueprint.route('/api/users/<int:users_id>', methods=['GET'])
def get_one_users(users_id):
    db_sess = db_session.create_session()
    users = db_sess.query(User).get(users_id)
    if not users:
        return make_response(jsonify({'error': 'Not found'}), 404)
    return jsonify(
        {
            'users': users.to_dict(only=(
                'id', 'surname', 'name', 'age', 'position', 'speciality', 'address', 'email', 'hashed_password',
                'modified_date'))
        }
    )


@blueprint.route('/api/users', methods=['POST'])
def create_users():
    if not request.json:
        return make_response(jsonify({'error': 'Empty request'}), 400)
    elif not all(key in request.json for key in
                 ['surname', 'name', 'age', 'position', 'speciality', 'address', 'email', 'hashed_password']):
        return make_response(jsonify({'error': 'Bad request'}), 400)
    db_sess = db_session.create_session()
    users = User(
        surname=request.json['surname'],
        name=request.json['name'],
        age=request.json['age'],
        position = request.json['position'],
        speciality = request.json['speciality'],
        address = request.json['address'],
        email = request.json['email'],
        hashed_password = request.json['hashed_password']
    )
    db_sess.add(users)
    db_sess.commit()
    return jsonify({'id': users.id})


@blueprint.route('/api/users/<int:users_id>', methods=['DELETE'])
def delete_users(users_id):
    db_sess = db_session.create_session()
    users = db_sess.query(User).get(users_id)
    if not users:
        return make_response(jsonify({'error': 'Not found'}), 404)
    db_sess.delete(users)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route("/api/users/edit/<int:user_id>", methods=['PUT'])
def user_edit(user_id):
    valid = ["surname", "name", "age",
             "position", "speciality", "address",
             "email", "hashed_password", 'modified_date']
    if not request.json:
        return jsonify({'error': 'Empty request'})
    db_sess = db_session.create_session()
    user = db_sess.query(User).filter(User.id == user_id)
    if not user.first():
        return make_response(jsonify({'error': 'Not found'}), 404)
    edits = {}
    for j in request.json:
        if j in valid:
            edits[j] = request.json[j]
    user.update(edits)
    db_sess.commit()
    return jsonify({'success': 'OK'})
