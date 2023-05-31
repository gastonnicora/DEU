from flask import jsonify,  request, abort
from app.models.config import Config
from app.helpers.Serializacion import Serializacion

def create():
    Config.create(request.get_json())
    return jsonify(),200

def index():
    users= Serializacion.dump(Config.all(),nombre="Configuraciones",many=True)
    return jsonify(users),200

def get(id): 
    user= Serializacion.dump(Config.get(id))
    return jsonify(user)

def update():
    Config.update(request.get_json())
    return jsonify(),200

def delete(id):
    Config.delete(id)
    return jsonify(),200

