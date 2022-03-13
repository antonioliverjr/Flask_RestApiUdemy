from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from data.context import Base
from entities.identity.roles_entity import RoleModel

class UserModel(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(12), unique=True, nullable=False)
    password = Column(String(150), nullable=False)
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(100))
    email = Column(String(100), nullable=False)
    role_id = Column(Integer, ForeignKey('roles.id'), nullable=False)
    ativo = Column(Boolean, default=False)

    role = relationship('RoleModel', backref='users')

    def __init__(self, username:str, password:str, firstname:str, email:str, role:RoleModel, id:int=None
    , lastname:str=None, role_id:int=None, ativo:bool=None) -> None:
        self.id = id
        self.username = username
        self.password = password
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.role_id = role_id
        self.ativo = ativo
        self.role = role

    def __str__(self) -> str:
        return f'{self.firstname} {self.lastname}' if f'{self.firstname} {self.lastname}' != '' else self.username