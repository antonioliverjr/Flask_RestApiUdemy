from sqlalchemy import Column, Integer, String
from data.context import Base


class RoleModel(Base):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True, autoincrement=True)
    role = Column(String(50), nullable=False)

    def __init__(self, role:str, id:int=None) -> None:
        self.id = id
        self.role = role.upper()

    def __str__(self) -> str:
        return self.role