from __future__ import annotations
from flask import request
from functools import wraps
from config.dependecy_injection import DependencyInjection
from services.identity.auth_service import AutheticationService
from services.identity.jwt_service import JwtService
from models.help_dto import HelpsDto
import jwt

DependencyInjection.register_ioc()
authService = AutheticationService()
jwtService = JwtService()

class Authenticate:
    def token(*role:str):
        def decorator(f):
            @wraps(f)
            def wrapper(*args, **kwargs):
                data = request.headers
                if not data['Bearer']:
                    return HelpsDto.message('Unauthorize Token Not Found'), 401
                try:
                    token = jwtService.validation_token(data['Bearer'])
                except jwt.ExpiredSignatureError:
                    return HelpsDto.message('Expired Token'), 401
                except jwt.InvalidAudienceError:
                    return HelpsDto.message('Expired Token'), 401

                user = authService.check_username(token['username'])
                if user is None:
                    return HelpsDto.message('User Not Found'), 401
                if role is not None:
                    if not user.role.role in [params.upper() for params in role]:
                        return HelpsDto.message('User does not have permission'), 401

                return f(*args, **kwargs)
            return wrapper
        return decorator

    @staticmethod
    def setting():
        authorizations = {
            'apiKey': {
                'type': 'apiKey',
                'in': 'header',
                'name': 'Bearer'
            }
        }
        return authorizations