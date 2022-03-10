from typing import Union, List
from data.context import Context
from data.interfaces.irole_repository import IRoleRepository
from entities.identity.roles_entity import RoleModel


class RoleRepository(IRoleRepository):
    def __init__(self) -> None:
        self.conn = Context()

    def get(self) -> List[RoleModel]:
        return self.conn.session.query(RoleModel).all()

    def get_id(self, id:int) -> Union[RoleModel, None]:
        return self.conn.session.query(RoleModel).filter_by(id=id).first()

    def search(self, role:str) -> Union[RoleModel, None]:
        return self.conn.session.query(RoleModel).filter(RoleModel.role == role.upper()).first()