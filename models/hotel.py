from enum import auto
from sqlalchemy import Column, ForeignKey, String, Integer, Float, Sequence
from sqlalchemy.orm import relationship
from data.context import Base
from models.city import CityModel


class HotelModel(Base):
    __tablename__ = 'hotels'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(80), nullable=False)
    stars = Column(Integer, nullable=False)
    daily = Column(Float(precision=2), nullable=False)
    city_id = Column(Integer, ForeignKey('cities.id'))

    city = relationship('CityModel', backref='hotels')

    def to_dict(self):
        return self.__dict__

    def __str__(self) -> str:
        return self.name+' - '+self.city.name
