from __future__ import annotations
from flask_restx import reqparse, fields
from marshmallow import Schema, fields as attr, validates, ValidationError
from models.identity.role_dto import role_dto


class UserDto:
    @staticmethod
    def request():
        args = reqparse.RequestParser()
        args.add_argument('username', type=str, required=True, trim=True, help='Report a Username is required', location='json')
        args.add_argument('password', type=str, required=True, help='Report a Password is required', location='json')
        args.add_argument('firstname', type=str, required=True, help='Firstname is Required', location='json')
        args.add_argument('lastname', type=str, default=None, help='Lastname is not required', location='json')
        args.add_argument('email', type=str, required=True, help='Email is required', location='json')
        return args

    @staticmethod
    def request_put():
        args = reqparse.RequestParser()
        args.add_argument('username', type=str, required=True, trim=True, help='Report a Username is required', location='json')
        args.add_argument('firstname', type=str, required=True, help='Firstname is Required', location='json')
        args.add_argument('lastname', type=str, default=None, help='Lastname is not required', location='json')
        args.add_argument('email', type=str, required=True, help='Email is required', location='json')
        return args

    @staticmethod
    def response():
        response = {
            'id': fields.Integer,
            'username': fields.String,
            'email': fields.String,
            'firstname': fields.String,
            'lastname': fields.String,
            'role': fields.Nested(role_dto),
            'ativo': fields.Boolean
        }
        return response


class AdminDto:
    @staticmethod
    def request():
        args = reqparse.RequestParser()
        args.add_argument('role', type=str, required=True, trim=True, help='Role is required', location='json')
        args.add_argument('ativo', type=bool, required=True, help='Active is required', location='json')
        return args

class ValidateUser(Schema):
    username =  attr.String()
    password = attr.String()
    email =  attr.Email()
    firstname = attr.String()
    lastname = attr.String()

    @validates('username')
    def validate_username(self, value):
        size = len(value)
        if size < 8 or size > 12:
            raise ValidationError('Username must contain between 8 to 12 characters.')
    
    @validates('password')
    def validate_password(self, value):
        size = len(value)
        if size < 6 or size > 12:
            raise ValidationError('Password must contain between 6 to 12 characters.')