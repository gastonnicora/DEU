from flask import Flask,jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from os import path, environ
import pymysql

from config import config
from app import db_config

def create_app(environment="development"):
    # Configuración inicial de la app
    app = Flask(__name__)
    app.config['CORS_HEADERS'] = 'Content-Type'
    cors = CORS(app, resources={r"/*": {"origins": "*"}})

    env = environ.get("FLASK_ENV", environment)
    app.config.from_object(config[env])

        
    app.config["SQLALCHEMY_DATABASE_URI"] = db_config.connection(app)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
    db = SQLAlchemy(app)

    @app.route("/")
    def home():
        return jsonify({"response": "hello word"})
    return app


