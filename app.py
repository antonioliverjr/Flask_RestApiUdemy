#from __future__ import annotations
from flask import Flask
from config.routers import Urls
from data.context import Context

app = Flask(__name__)

Urls.routers(app)

if __name__ == '__main__':
    Context.init_database()
    app.run(debug=True)
