from flask import Flask
from config.routers import Urls
from config.swagger_ui import SwaggerUi

app = Flask(__name__)

Urls.routers(app)

SwaggerUi.init(app)

if __name__ == '__main__':
    app.run(debug=True)
