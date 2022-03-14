from flask_restx import Namespace, Resource, marshal
from config.dependecy_injection import DependencyInjection
from models.identity.user_dto import UserDto, AdminDto ,ValidateUser
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

user_dto = user.model('user', UserDto.response())
token_dto = token.model('token', TokenDto.response())

@user.route('/admin')
class AdminController(Resource):
    @user.doc('Return User List')
    @user.expect(HelpsDto.pagination())
    @user.response(code=200, description='User list is Successfully return.', model=[user_dto]) 
    @user.response(code=404, description='User list is empty')
    @Authorize.token('admin')
    def get(self):
        '''Return User List pagination'''
        args = HelpsDto.pagination()
        data = args.parse_args()
        users = authService.return_list_user(**data)
        if len(users) != 0:            
            return marshal(users, user_dto), 200
        else:
            return marshal(users, user_dto), 404

@user.route('/admin/<int:id>')
@user.param('id', 'User Id')
class AdminController(Resource):
    @user.doc('Return User')
    @user.response(code=200, description='User successfully return.', model=user_dto)
    @user.response(code=404, description='The User is not created in Users')
    @Authorize.token('admin')
    def get(self, id:int):
        '''Return User'''
        user = authService.return_user(id)
        if user is None:
            return HelpsDto.message(f'Id not found, Id: {id} was provided.'), 404
        return marshal(user, user_dto), 200

    @user.doc('Authorize User')
    @user.expect(AdminDto.request())
    @user.response(code=200, description='User successfully return.', model=user_dto)
    @user.response(code=400, description='There was an error updating the service')
    @user.response(code=404, description='The User is not created in Users')
    @Authorize.token('admin')
    def put(self, id:int):
        '''Update permission by user and active'''
        args = AdminDto.request()
        data = args.parse_args()
        user = authService.return_user(id)
        if user is None:
            return HelpsDto.message(f'Id not found, Id: {id} was provided.'), 404
        role = authService.check_role(data['role'])
        if role is None:
            return HelpsDto.message(f'Role not found.'), 404
        data['id'] = id
        data['username'] = user.username
        data['firstname'] = user.firstname
        data['lastname'] = user.lastname
        data['email'] = user.email
        data['role_id'] = role.id
        try:
            user_result = authService.update_user(**data)
        except Exception as ex:
            return HelpsDto.message(str(ex)), 400
        return marshal(user_result, user_dto), 200
    
    @user.doc('Remove a User')
    @user.response(code=200, description='User removed successfully.')
    @user.response(code=400, description='There was an error removed the service')
    @user.response(code=404, description='The User is not created in Users')
    @Authorize.token('admin')
    def delete(self, id:int):
        '''Remove a user'''
        if authService.return_user(id):
            try: 
                result = authService.delete_user(id)
            except Exception as ex:
                return HelpsDto.message(str(ex)), 400
            if result:
                return HelpsDto.message('User removed successfully.'), 200
        return HelpsDto.message(f'Id not found, Id: {id} was provided.'), 404

@user.route('/register')
class UserController(Resource):
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
class UserControllerId(Resource):
    @user.doc('Confirmação de E-mail')
    def get(self, id:int):
        pass

    @user.doc('Updating User')
    @user.expect(UserDto.request_put())
    @user.response(code=201, description='User Successfully Updating.', model=user_dto)
    @user.response(code=400, description='There was an error updating in the service.')
    @user.response(code=404, description='The User is not created in Users')
    @Authorize.token('user',user_confirmed=True)
    def put(self, id:int):
        args = UserDto.request_put()
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

        