from flask import Flask
from flask_restx import Api


class Settings:
    @staticmethod
    def app_config(app:Flask) -> Flask:
        app.config.update(
            RESTX_MASK_SWAGGER=False,
        )
        return app

    @staticmethod
    def api_config(app:Flask) -> Api:
        api = Api(
            app,
            openapi='3.0.1',
            version='1.0.0',
            title='Clean Python API',
            description='API baseada na Clean Architeture com Python',
            contact='Antonio Oliveira',
            contact_email='antoniobatistajr@gmail.com',
        )
        return api

    @staticmethod
    def add_routes(api:Api, *args) -> Api:
        for arg in args:
            api.add_namespace(arg)
        return api
        
