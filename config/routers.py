from flask import Flask
from flask_restful import Api
from controllers.hotel import HotelController
from controllers.city import CityController


class Urls:
    @staticmethod
    def routers(app:Flask):
        api = Api(app)
        api.add_resource(HotelController, '/hotels', '/hotels/<int:id>')
        api.add_resource(CityController, '/cities', '/cities/<int:id>')

        return api