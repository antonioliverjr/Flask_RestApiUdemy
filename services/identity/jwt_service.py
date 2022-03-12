from typing import Union
from datetime import datetime, timedelta
from data.interfaces.iuser_repository import IUserRepository
from data.interfaces.irole_repository import IRoleRepository
from entities.identity.user_entity import UserModel
from decouple import config
import inject
import jwt


class JwtService:
    @inject.autoparams()
    def __init__(self, userRepository: IUserRepository, roleRepository: IRoleRepository) -> None:
        self.userRepository = userRepository()
        self.roleRepository = roleRepository()

    def generation_token(self, user:UserModel) -> str:
        return jwt.encode(
            {
                'username': user.username,
                'email': user.email if user.email is not None else 'N/A',
                'exp': datetime.utcnow() + timedelta(seconds=60),
                'aud': config('AUDIENCE')
            },
            config('SECRET-KEY'),
            algorithm='HS256'
        )
    
    def validation_token(self, token:str) -> Union[str, jwt.ExpiredSignatureError, jwt.InvalidAudienceError, Exception]:
        try:
            token_decode = jwt.decode(token, config('SECRET-KEY'), audience='http://wwww.olinfor.com.br', algorithms='HS256')
        except jwt.ExpiredSignatureError:
            raise jwt.ExpiredSignatureError
        except jwt.InvalidAudienceError:
            raise jwt.InvalidAudienceError
        return token_decode

    def validation_user(self, username:str) -> Union[UserModel, None]:
        return self.userRepository.search(username)
