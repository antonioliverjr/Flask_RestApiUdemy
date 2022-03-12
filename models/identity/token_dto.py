from flask_restx import reqparse, fields


class TokenDto:
    @staticmethod
    def request():
        args = reqparse.RequestParser()
        args.add_argument('username', type=str, default=None, case_sensitive=True, help='Report Username or Email', location='json')
        args.add_argument('email', type=str, default=None, case_sensitive=True, help='Report Username or Email', location='json')
        args.add_argument('password', type=str, required=True, help='Password is required', location='json')
        return args

    @staticmethod
    def response():
        response = {
            'token': fields.String 
        }
        return response
