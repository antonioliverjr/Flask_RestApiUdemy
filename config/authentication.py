from flask import Flask


class Authenticate:
    @staticmethod
    def init_jwt(app: Flask):
        pass

    @staticmethod
    def get_auth():
        authorizations = {
            'apiKey': {
                'type': 'apiKey',
                'in': 'header',
                'name': 'Bearer'
            }
        }
        return authorizations