from flask import Flask
from flask_restful import Api
from resources.hotel import HotelController


class Urls:
    @staticmethod
    def routers(app:Flask):
        api = Api(app)
        api.add_resource(HotelController, '/hotels', '/hotels/<int:id>')

        return api