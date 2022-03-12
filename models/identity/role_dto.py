from flask_restx import reqparse, fields, Namespace

role = Namespace('role', description='Roles Operations')

class RoleDto:
    @staticmethod
    def request():
        args = reqparse.RequestParser()
        args.add_argument('role', type=str, required=True, help='Role is required')
        return args

    @staticmethod
    def response():
        response = {
            'id': fields.Integer,
            'role': fields.String
        }
        return response

role_dto = role.model('role', RoleDto.response())