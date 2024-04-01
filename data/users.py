import sqlalchemy
from flask_login import UserMixin
from sqlalchemy_serializer import SerializerMixin
from werkzeug.security import generate_password_hash, check_password_hash

from sqlalchemy import orm, ext

from .db_session import SqlAlchemyBase


# Модель Марсиане
class User(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    surname = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    age = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    position = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    speciality = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    address = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True, nullable=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    modified_date = sqlalchemy.Column(sqlalchemy.DateTime)
    #city_from = sqlalchemy.Column(sqlalchemy.String, default='Moscow')

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)

    def __str__(self):
        return "<colonist> " + str(self.id) + " " + self.surname + " " + self.name

    def __repr__(self):
        return (f"{self.surname} {self.name} {self.age} {self.position} {self.speciality} {self.address} {self.email}"
                f" {self.hashed_password}")

    jobs = orm.relationship("Jobs", back_populates='user')
    departments = orm.relationship("Department", back_populates='user')