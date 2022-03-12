from __future__ import annotations
from flask_restx import reqparse, fields
from models.identity.role_dto import role_dto


class UserDto:
    @staticmethod
    def request():
        args = reqparse.RequestParser()
        args.add_argument('username', type=str, required=True, trim=True, help='Report a Username is required')
        args.add_argument('password', type=str, required=True, help='Report a Password is required')
        args.add_argument('firstname', type=str, required=True, help='Firstname is Required')
        args.add_argument('lastname', type=str, help='Lastname is not required')
        args.add_argument('email', type=str, required=True, help='Email is required')
        args.add_argument('role', type=str, required=True, help='Report a Role for User')
        return args

    @staticmethod
    def response():
        response = {
            'id': fields.Integer,
            'username': fields.String,
            'email': fields.String,
            'firstname': fields.String,
            'lastname': fields.String,
            'role': fields.Nested(role_dto)
        }
        return response
