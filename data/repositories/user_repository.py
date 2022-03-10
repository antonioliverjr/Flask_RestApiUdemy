from typing import Union, List
from data.context import Context
from werkzeug.security import generate_password_hash
from data.interfaces.iuser_repository import IUserRepository
from data.repositories.role_repository import RoleRepository
from entities.identity.user_entity import UserModel
from entities.identity.roles_entity import RoleModel

__roleRepository = RoleRepository()

class UserRepository(IUserRepository):
    def __init__(self) -> None:
        self.conn = Context()

    def get(self, offset:int, limit:int) -> List[UserModel]:
        offset = (offset - 1) * limit
        return self.conn.session.query(UserModel).offset(offset).limit(limit).all()

    def get_id(self, id:int) -> Union[UserModel, None]:
        return self.conn.session.query(UserModel).filter_by(id=id).first()

    def add(self, username:str, password:str, firstname:str, email:str, role:str, lastname:str=None) -> Union[UserModel, Exception]:
        role_obj = __roleRepository.search(role)
        if role_obj is None:
            raise ValueError('Role Not Found')
        user = UserModel(username.lower(), generate_password_hash(password), firstname.upper(), email.lower(), role_obj, lastname=lastname.upper() if lastname is not None else None)
        try:
            self.conn.session.add(user)
            self.conn.save()
        except Exception as ex:
            return ex
        return self.search(username)

    def update(self, id:int, **user) -> Union[UserModel, Exception]:
        role = __roleRepository.search(user['role'])
        if not role:
            raise ValueError('Role Not Found')
        try:
            self.conn.session.query(UserModel).filter_by(id=id).update(
                {
                    'username': user['username'].lower(),
                    'password': generate_password_hash(user['password']),
                    'firstname': user['firstname'].upper(),
                    'email': user['email'].lower(),
                    'role_id': role.id,
                    'lastname': user['lastname'].upper(),
                    'status': user['status']
                }, synchronize_session=False
            )
            self.conn.save()
        except Exception as ex:
            return ex
        return self.get_id(id)

    def delete(self, id:int) -> Union[bool, Exception]:
        try:
            self.conn.session.query(UserModel).filter_by(id=id).delete(synchronize_session=False)
            self.conn.save()
        except Exception as ex:
            return ex
        return True

    def search(self, username:str) -> Union[UserModel, None]:
        return self.conn.session.query(UserModel).filter(UserModel.username == username.lower()).first()