from sqlalchemy import Column, ForeignKey, String, Integer, Float, Boolean
from sqlalchemy.orm import relationship
from data.context import Base
from models.city_model import CityModel


class HotelModel(Base):
    __tablename__ = 'hotels'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(80), nullable=False)
    stars = Column(Integer, nullable=False)
    daily = Column(Float(precision=2), nullable=False)
    status = Column(Boolean, default=True)
    city_id = Column(Integer, ForeignKey('cities.id'), nullable=False)

    city = relationship('CityModel', backref='hotels')

    def __init__(self, name:str, stars:int, daily:float, city:CityModel
    , city_id:int=None, id:int=None, status:bool=None) -> None:
        self.id = id
        self.name = name.upper()
        self.stars = stars
        self.daily = daily
        self.city_id = city_id
        self.city = city
        self.status = status

    def to_dict(self):
        return self.__dict__

    def __str__(self) -> str:
        return self.name+' - '+self.city.name
