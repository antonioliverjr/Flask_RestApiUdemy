from flask import Flask
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec
from controllers.__controllers_all import *


class SwaggerUi:
    @staticmethod
    def init(app:Flask):
        app.config.update({
            'APISPEC_SPEC': APISpec(
                title='Clean Python Base API',
                version='v1',
                openapi_version='3.0.0',
                plugins=[MarshmallowPlugin()],
                description='Criando modelo base API Clean Architeture',
                termsOfService='',
                contact={
                    'name': 'Antonio Oliveira',
                    'url': '',
                    'email': 'antoniobatistajr@gmail.com'
                },
                license={
                'name': 'MIT',
                'url': 'https://opensource.org/licenses/MIT'
                },
            ),
            'APISPEC_SWAGGER_URL': '/swagger-json/',
            'APISPEC_SWAGGER_UI_URL': '/swagger/'
        })
    
        docs = FlaskApiSpec(app)

        docs.register(HotelController)
        docs.register(HotelControllerId)
        docs.register(CityController)
        docs.register(CityControllerId)

        return app
