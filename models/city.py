from sqlalchemy import Column, String, Integer
from data.context import Base


class CityModel(Base):
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    uf = Column(String(2), nullable=False)

    def __init__(self, name:str, uf:str, id:int=None) -> None:
        self.id = id
        self.name = name.upper()
        self.uf = uf.upper()

    def to_dict(self):
        return self.__dict__
    
    def __str__(self) -> str:
        return self.name+'-'+self.uf
