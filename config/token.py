from decouple import config


class Authenticate:
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