from flask import Flask
from flask_restful import Api
from controllers.__controllers_all import *


class Urls:
    @staticmethod
    def routers(app:Flask):
        api = Api(app)
        api.add_resource(HotelController, '/hotels')
        api.add_resource(HotelControllerId, '/hotels/<int:id>')
        api.add_resource(CityController, '/cities')
        api.add_resource(CityControllerId, '/cities/<int:id>')

        return api