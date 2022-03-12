from flask_restx import Namespace, Resource, marshal
from config.dependecy_injection import DependencyInjection
from models.identity.user_dto import UserDto
from models.identity.role_dto import RoleDto
from models.identity.token_dto import TokenDto
from models.help_dto import HelpsDto
from services.identity.auth_service import AutheticationService
from services.identity.jwt_service import JwtService
from config.jwt import Authenticate

user = Namespace('user', description='Users operation Register, Logout')
token = Namespace('token', description='Authentication routes by Login e Generation Token')
DependencyInjection.register_ioc()
authService = AutheticationService()
jwtService = JwtService()

user_dto = user.model('users', UserDto.response())
token_dto = token.model('token', TokenDto.response())

@user.route('/register')
class UserController(Resource):
    @Authenticate.token('user')
    def get(self):
        return HelpsDto.message('Logou'), 200

    def post(self):
        pass

    def update(self):
        pass

@token.route('/')
class TokenController(Resource):
    @token.doc('Token Generation')
    @token.expect(TokenDto.request())
    @token.response(code=201, description='Token Created Successfully', model=token_dto)
    @token.response(code=400, description='Login data missing')
    @token.response(code=401, description='Authorization Error')
    def post(self):
        args = TokenDto.request()
        data = args.parse_args()
        if data['username'] is None and data['email'] is None:
            return HelpsDto.message('Enter a Username or Email for login and Token Generation.'), 400
        user = authService.login_user(**data)
        if user is None:
            return HelpsDto.message('User Not Found or Password not validated.'), 401
        return jwtService.generation_token(user)
        