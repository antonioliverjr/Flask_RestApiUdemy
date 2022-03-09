from marshmallow import Schema, fields, validates, ValidationError


class MessageResponseDto(Schema):
    message = fields.String(default='Success')


class PaginationArgsDto(Schema):
    page = fields.Integer(missing=1)
    limit = fields.Integer(missing=25)

    @validates('page')
    def validate_page(self, value):
        if value < 1:
            raise ValidationError('Page is not a value reference.')

    @validates('limit')
    def validate_limit(self, value):
        if value < 1:
            raise ValidationError('Limit is not a value reference.')

class RouteArgsDto(Schema):
    id = fields.Integer()
