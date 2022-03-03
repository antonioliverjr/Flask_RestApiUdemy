from typing import List
from config.context import sql
from models.city import CityModel

cities = sql.Table('cities',
    sql.Column('hotel_id', sql.Integer, sql.ForeignKey('hotels.id'), primary_key=True),
    sql.Column('city_id', sql.Integer, sql.ForeignKey('city.id'), primary_key=True)
)

class HotelModel(sql.Model):
    __tablename__ = 'hotels'

    id = sql.Column(sql.String, primary_key=True)
    name = sql.Column(sql.String(80))
    stars = sql.Column(sql.Integer)
    daily = sql.Column(sql.Float(precision=2))
    cities = sql.relationship('city', secondary=cities, lazy='subquery',
        backref=sql.backref('hotels', lazy=True))

    '''
    def __init__(self, name:str, stars:int, daily:str, city:List[CityModel]) -> None:
        self.name = name
        self.stars = stars
        self.daily = daily
        self.city = city

    def to_dict(self):
        return self.__dict__
    '''