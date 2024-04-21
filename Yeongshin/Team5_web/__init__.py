from flask import Flask
import mysql.connector
from flask import render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import pyttsx3
from PIL import Image
import io
import base64
from .utils import image_to_binary

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # MySQL 데이터베이스 연결
    app.config.from_pyfile('config.py')
    db.init_app(app)
    migrate.init_app(app, db)


    from .views import main
    app.register_blueprint(main.bp)


    return app
