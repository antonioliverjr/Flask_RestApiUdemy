from marshmallow import Schema, fields


class CityRequestDto(Schema):
    name = fields.String(required=True, description='Name is required.')
    uf = fields.String(required=True, description='Uf is required.')

class CityResponseDto(Schema):
    id = fields.Integer()
    name = fields.String()
    uf = fields.String()
