import inject
from entities.identity.user_entity import UserModel
from data.interfaces.iuser_repository import IUserRepository
from data.interfaces.irole_repository import IRoleRepository


class AutheticationService:
    @inject.autoparams()
    def __init__(self, userRepository: IUserRepository, roleRepository: IRoleRepository) -> None:
        self.userRepository = userRepository
        self.roleRepository = roleRepository

    def register_user(self) -> UserModel:
        pass

    def login_user(self) -> UserModel:
        pass

    def generation_token(self) -> str:
        pass

    def logout(self) -> None:
        pass

