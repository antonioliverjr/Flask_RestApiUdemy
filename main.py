from flask import Flask
from config.settings import Settings
from controllers.__controllers_all import *

app = Flask(__name__)

Settings.app_config(app)

api = Settings.api_config(app)

Settings.add_routes(api, hotel, city)

if __name__ == '__main__':
    app.run(debug=True)