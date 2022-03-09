from flask import Flask
from flask_restx import Api


class _Server():
    def __init__(self) -> None:
        self.app = Flask(__name__)
        self.app.config.update(
            RESTX_MASK_SWAGGER=False,
        )
        self.api = Api(
            self.app,
            openapi='3.0.1',
            version='1.0.0',
            title='Clean Python API',
            description='API baseada na Clean Architeture com Python',
            contact='Antonio Oliveira',
            contact_email='antoniobatistajr@gmail.com',
        )
    
    def run(self):
        self.app.run(debug=True)

server = _Server()