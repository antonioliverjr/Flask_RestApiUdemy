from typing import Union, List
from werkzeug.security import check_password_hash
from entities.identity.roles_entity import RoleModel
from entities.identity.user_entity import UserModel
from data.interfaces.iuser_repository import IUserRepository
from data.interfaces.irole_repository import IRoleRepository
import inject


class AutheticationService:
    @inject.autoparams()
    def __init__(self, userRepository: IUserRepository, roleRepository: IRoleRepository) -> None:
        self.userRepository = userRepository()
        self.roleRepository = roleRepository()

    def check_username(self, username:str) -> Union[UserModel, None]:
        return self.userRepository.search(username)
        
    def check_role(self, role_name:str) -> bool:
        if self.roleRepository.search(role_name):
            return True
        return False

    def return_user(self, id:int) -> Union[UserModel, None]:
        return self.userRepository.get_id(id)

    def return_role(self, id:int) -> Union[RoleModel, None]:
        return self.roleRepository.get_id(id)

    def return_list_user(self, page:int, limit:int) -> List[UserModel]:
        return self.userRepository.get(offset=page, limit=limit)

    def return_list_role(self) -> List[RoleModel]:
        return self.roleRepository.get()
    
    def register_user(self, **data) -> Union[UserModel, Exception]:
        return self.userRepository.add(**data)

    def update_user(self, **data) -> Union[UserModel, Exception]:
        return self.userRepository.update(**data)

    def login_user(self, password:str, username:str=None, email:str=None) -> Union[UserModel, None]:
        user = self.userRepository.search(username, email)
        if not user:
            return None
        if check_password_hash(user.password, password):
            return user
        return None
