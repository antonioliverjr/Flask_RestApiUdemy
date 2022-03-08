from marshmallow import Schema, fields


class MessageResponseDto(Schema):
    message = fields.String(default='Success')
