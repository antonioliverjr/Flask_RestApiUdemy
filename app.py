from flask import Flask
from config.routers import Urls
from config.context import Context, sql

app = Flask(__name__)
Context.config(app)

@app.before_first_request
def create_database():
    sql.create_all()

Urls.routers(app)

if __name__ == '__main__':
    sql.init_app(app)
    app.run(debug=True)
