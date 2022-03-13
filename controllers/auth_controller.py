from flask_restx import Namespace, Resource, marshal
from config.dependecy_injection import DependencyInjection
from models.identity.user_dto import UserDto, ValidateUser
from models.identity.role_dto import RoleDto
from models.identity.token_dto import TokenDto
from models.help_dto import HelpsDto
from services.identity.auth_service import AutheticationService
from services.identity.jwt_service import JwtService
from config.jwt import Authorize

user = Namespace('user', description='Users operation Register, Logout')
token = Namespace('token', description='Authentication routes by Login e Generation Token')
DependencyInjection.register_ioc()
authService = AutheticationService()
jwtService = JwtService()

user_dto = user.model('users', UserDto.response())
token_dto = token.model('token', TokenDto.response())

@user.route('/register')
class UserController(Resource):
    @Authorize.token('user')
    def get(self):
        return HelpsDto.message('Logou'), 200

    @user.doc('Register User')
    @user.expect(UserDto.request())
    @user.response(code=201, description='User Successfully Create.', model=user_dto)
    @user.response(code=400, description='There was an error creating in the service.')
    def post(self):
        args = UserDto.request()
        req = args.parse_args()
        try:
            data = ValidateUser().load(req)
        except Exception as ex:
            return HelpsDto.message(str(ex)), 400
        try:
            user = authService.register_user(**data)
        except Exception as ex:
            return HelpsDto.message(str(ex)), 400
        return marshal(user, user_dto), 201


@user.route('/register/<int:id>')
@user.param('id', 'User Id')
class UserController(Resource):
    @user.doc('Register User')
    @user.expect(UserDto.request())
    @user.response(code=201, description='User Successfully Updating.', model=user_dto)
    @user.response(code=400, description='There was an error updating in the service.')
    @user.response(code=404, description='The User is not created in Users')
    def put(self, id:int):
        args = UserDto.request()
        req = args.parse_args()
        try:
            data = ValidateUser().load(req)
        except Exception as ex:
            return HelpsDto.message(str(ex)), 400

        if not authService.return_user(id): return HelpsDto.message(f'Id not found, Id:{id} was provided.'), 404
        
        try:
            data['id'] = id
            user = authService.update_user(**data)
        except Exception as ex:
            return HelpsDto.message(str(ex)), 400
        return marshal(user, user_dto), 201

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
        if not user.ativo:
            return HelpsDto.message('User is not active'), 401
        return jwtService.generation_token(user)
        