from flask_restful import fields
from abc import ABC, abstractmethod,abstractstaticmethod


class BaseDto(ABC):
    @abstractmethod
    def request(): pass

    @abstractmethod
    def response(): pass

    @abstractstaticmethod
    def message():
        message = {
            'message': fields.String
        }
        return message
