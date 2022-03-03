from flask import Flask
from flask_sqlalchemy import SQLAlchemy

sql = SQLAlchemy()

class Context:
    @staticmethod
    def config(app:Flask):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        return app