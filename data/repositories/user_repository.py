from typing import Union, List
from sqlalchemy import or_
from data.context import Context
from werkzeug.security import generate_password_hash
from data.interfaces.iuser_repository import IUserRepository
from entities.identity.user_entity import UserModel
from entities.identity.roles_entity import RoleModel


class UserRepository(IUserRepository):
    def __init__(self) -> None:
        self.conn = Context()

    def get(self, offset:int, limit:int) -> List[UserModel]:
        offset = (offset - 1) * limit
        return self.conn.session.query(UserModel).offset(offset).limit(limit).all()

    def get_id(self, id:int) -> Union[UserModel, None]:
        return self.conn.session.query(UserModel).filter_by(id=id).first()

    def add(self, username:str, password:str, firstname:str, email:str, lastname:str=None) -> Union[UserModel, Exception]:
        role = self.conn.session.query(RoleModel).filter_by(role='USER').first()
        user = UserModel(username.lower(), generate_password_hash(password), firstname.upper()
        , email.lower(), role, lastname=lastname.upper() if lastname is not None else None)
        try:
            self.conn.session.add(user)
            self.conn.save()
        except Exception as ex:
            return ex
        return self.search(username)

    def update(self, **user) -> Union[UserModel, Exception]:
        if user.get('ativo'):
            try:
                self.conn.session.query(UserModel).filter_by(id=user['id']).update(
                    {
                        'username': user['username'].lower(),
                        'firstname': user['firstname'].upper(),
                        'email': user['email'].lower(),
                        'lastname': user['lastname'].upper(),
                        'role_id': user['role_id'],
                        'ativo': user['ativo'] 
                    }, synchronize_session=False
                )
                self.conn.save()
            except Exception as ex:
                    return ex
        
        try:
            self.conn.session.query(UserModel).filter_by(id=user['id']).update(
                {
                    'username': user['username'].lower(),
                    'firstname': user['firstname'].upper(),
                    'email': user['email'].lower(),
                    'lastname': user['lastname'].upper(),
                }, synchronize_session=False
            )
            self.conn.save()
        except Exception as ex:
            return ex
        return self.get_id(user['id'])

    def delete(self, id:int) -> Union[bool, Exception]:
        try:
            self.conn.session.query(UserModel).filter_by(id=id).delete(synchronize_session=False)
            self.conn.save()
        except Exception as ex:
            return ex
        return True

    def search(self, username:str, email:str=None) -> Union[UserModel, None]:
        return self.conn.session.query(UserModel).filter(
            or_(UserModel.username == username, UserModel.email == email)
        ).first()