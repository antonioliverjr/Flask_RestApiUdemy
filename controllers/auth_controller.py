from flask_restx import Namespace, Resource, marshal
from config.dependecy_injection import DependencyInjection
from services.identity.auth_service import AutheticationService

user = Namespace('user', description='Users operation Register, Logout')
token = Namespace('token', description='Authentication routes by Login e Generation Token')
DependencyInjection.register_ioc()
authService = AutheticationService()

user_dto = ''
token_dto = ''

@user.route('/register')
class UserController(Resource):
    def get(self):
        pass

    def post(self):
        pass

@user.route('/logout')
class LogoutController(Resource):
    def get(self):
        pass

@token.route('/')
class TokenController(Resource):
    def post(self):
        pass