from marshmallow import Schema, fields
from views.city_dto import CityResponseDto


class HotelRequestDto(Schema):
    name = fields.String(required=True, description='Name is required and only string')
    stars = fields.Integer(required=True, description='Stars is required and only integer')
    daily = fields.Float(required=True, description='Daily is required and only decimal')
    city = fields.String(required=True, description='City is required and only string')
    status = fields.Boolean(description='Status is not required and default value is True')


class HotelResponseDto(Schema):
    id = fields.Integer()
    name = fields.String()
    stars = fields.Integer()
    daily = fields.Float()
    city = fields.Nested(CityResponseDto)
    status = fields.Boolean()
        