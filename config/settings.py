from __future__ import annotations
from flask import Flask
from flask_restx import Api
from config.authentication import Authenticate
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
            security=['http'],
            authorizations=Authenticate.get_auth()
        )
        return api
    
    @staticmethod
    def add_routes(api:Api, *namespaces) -> Api:
        for names_list in namespaces:
            for namespace in names_list:
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
