from flask import Flask
from config.settings import Settings
from config.dependecy_injection import DependencyInjection
from controllers.__controllers_all import *

app = Flask(__name__)

Settings.app_config(app)

api = Settings.api_config(app)

Settings.add_routes(api, hotel, city)

Settings.seed_roles()
Settings.seed_users()



if __name__ == '__main__':
    app.run(debug=True)