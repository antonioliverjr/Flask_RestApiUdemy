from __future__ import annotations
from flask import Flask
from flask_restx import Api
from config.jwt import Authorize
from services.identity.seed_user_roles import SeedUserRolesInitial


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
            security=['apiKey'],
            authorizations=Authorize.setting()
        )
        return api
    
    @staticmethod
    def add_routes(api:Api, *namespaces) -> Api:
        for list in namespaces:
            for namespace in list:
                api.add_namespace(namespace)
        return api

    @staticmethod
    def seed_roles():
        seed = SeedUserRolesInitial()
        seed.seed_roles()

    @staticmethod
    def seed_users():
        seed = SeedUserRolesInitial()
        seed.seed_users()
