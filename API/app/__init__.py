from flask import Flask,jsonify, request, render_template
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from os import path, environ
from  app.resources import usuario, ejercicio, video,entrenamiento, ent_eje, ent_alu,config, entrenador_alumno,config as c
import socket

from config import config
from app import db_config
from app.models.modelos import db


def create_app(environment="production"):
    # Configuración inicial de la app
    app = Flask(__name__) 
    app.config['CORS_HEADERS'] = 'Content-Type'
    cors = CORS(app)

    env = environ.get("FLASK_ENV", environment)
    app.config.from_object(config[env])

    app.config["SQLALCHEMY_DATABASE_URI"] = db_config.connection(app)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
 
    # Rutas API-REST
    app.add_url_rule("/usuarios", "usuarios", usuario.index)
    app.add_url_rule("/usuario/<int:id>", "usuario_get", usuario.get)
    app.add_url_rule("/usuario","usuario_post",usuario.create,methods=["POST"])
    app.add_url_rule("/usuario_editar","usuario_put",usuario.update,methods=["POST"])
    app.add_url_rule("/usuario_editar_pass","usuario_put_pass",usuario.update_pass,methods=["POST"])
    app.add_url_rule("/usuario_borrar/<int:id>", "usuario_delete", usuario.delete)
    app.add_url_rule("/usuario/alumnos/<int:id>", "usuario_get_alumnos", usuario.get_alumnos)
    app.add_url_rule("/usuario/alumnos", "usuario_alumnos", usuario.alumnos) #falta
    app.add_url_rule("/login","login",usuario.login,methods=["POST"])
    
    app.add_url_rule("/ejercicios", "ejercicios", ejercicio.index)
    app.add_url_rule("/ejercicio/<int:id>", "ejercicio_get", ejercicio.get)
    app.add_url_rule("/ejercicio_by_entrenador/<int:id>", "ejercicio_get_by_entrenador", ejercicio.get_by_entrenador)
    app.add_url_rule("/ejercicio","ejercicio_post",ejercicio.create,methods=["POST"])
    app.add_url_rule("/ejercicio_editar","ejercicio_put",ejercicio.update,methods=["POST"])
    app.add_url_rule("/ejercicio_borrar/<int:id>", "ejercicio_delete", ejercicio.delete)
    
    
    app.add_url_rule("/videos", "videos", video.index)
    app.add_url_rule("/video/<int:id>", "video_get", video.get)
    app.add_url_rule("/video","video_post",video.create,methods=["POST"])
    app.add_url_rule("/video_editar","video_put",video.update,methods=["POST"])
    app.add_url_rule("/video_borrar/<int:id>", "video_delete", video.delete)
    
    app.add_url_rule("/entrenamientos", "entrenamientos", entrenamiento.index)
    app.add_url_rule("/entrenamiento/<int:id>", "entrenamiento_get", entrenamiento.get)
    app.add_url_rule("/entrenamiento","entrenamiento_post",entrenamiento.create,methods=["POST"])
    app.add_url_rule("/entrenamiento_editar","entrenamiento_put",entrenamiento.update,methods=["POST"])
    app.add_url_rule("/entrenamiento_borrar/<int:id>", "entrenamiento_delete", entrenamiento.delete)
    app.add_url_rule("/entrenamiento_by_entrenador/<int:id>", "entrenamiento_get_by_entrenador", entrenamiento.get_by_entrenador)
    app.add_url_rule("/entrenamiento_by_alumno/<int:id>", "entrenamiento_get_by_alumno", entrenamiento.get_entrenamientos_by_alumno)
    
    app.add_url_rule("/ent_ejes", "ent_ejes", ent_eje.index)
    app.add_url_rule("/ent_eje/<int:id>", "ent_eje_get", ent_eje.get)
    app.add_url_rule("/ent_eje","ent_eje_post",ent_eje.create,methods=["POST"])
    app.add_url_rule("/ent_eje_editar","ent_eje_put",ent_eje.update,methods=["POST"])
    app.add_url_rule("/ent_eje_borrar/<int:id>", "ent_eje_delete", ent_eje.delete)
    
    app.add_url_rule("/ent_alus", "ent_alus", ent_alu.index)
    app.add_url_rule("/ent_alu/<int:id>", "ent_alu_get", ent_alu.get)
    app.add_url_rule("/ent_alu","ent_alu_post",ent_alu.create,methods=["POST"])
    app.add_url_rule("/ent_alu_editar","ent_alu_put",ent_alu.update,methods=["POST"])
    app.add_url_rule("/ent_alu_editar_alu","ent_alu_put_alu",ent_alu.update_alu,methods=["POST"])
    app.add_url_rule("/ent_alu_editar_entrenador","ent_alu_put_entrenador",ent_alu.update_entrenador,methods=["POST"])
    app.add_url_rule("/ent_alu_borrar/<int:id>", "ent_alu_delete", ent_alu.delete)
    
    
    app.add_url_rule("/configs", "configs", c.index)
    app.add_url_rule("/config/<int:id>", "config_get", c.get)
    app.add_url_rule("/configByUser/<int:id>", "config_getByUser", c.getByUser)
    app.add_url_rule("/config","config_post",c.create,methods=["POST"])
    app.add_url_rule("/config_editar","config_put",c.update,methods=["POST"])
    app.add_url_rule("/config_borrar/<int:id>", "config_delete", c.delete)
    
    
    app.add_url_rule("/entrenador_alumnos", "entrenador_alumnos", entrenador_alumno.index)
    app.add_url_rule("/entrenador_alumno/<int:id>", "entrenador_alumno_get", entrenador_alumno.get)
    app.add_url_rule("/entrenador_alumno","entrenador_alumno_post",entrenador_alumno.create,methods=["POST"])
    app.add_url_rule("/entrenador_alumno_editar","entrenador_alumno_put",entrenador_alumno.update,methods=["POST"])
    app.add_url_rule("/entrenador_alumno_borrar/<int:id>", "entrenador_alumno_delete", entrenador_alumno.delete)
    
    @app.route("/")
    def home():
        return render_template("home.html")

    
    return app 


