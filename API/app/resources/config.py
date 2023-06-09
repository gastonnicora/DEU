from flask import jsonify,  request, abort
from app.models.config import Config
from app.helpers.Serializacion import Serializacion
import json

def create():
    c=Config.create(request.get_json())
    if c is None:
        return jsonify({"error":"no se pudo guardar la configuración"}),400
    return jsonify(c.toJSON()),200

def index():
    users= Serializacion.dump(Config.all(),nombre="Configuraciones",many=True)
    return jsonify(users),200

def get(id): 
    user=Config.get(id)
    if user is None:
        return jsonify({"error":" La configuración no existe"}),400
    return jsonify( Serializacion.dump(user))

def update():
    c= Config.update(request.get_json())
    if c is None:
        return jsonify({"error":"no se pudo editar la configuración"}),400
    return jsonify(c.toJSON()),200

def delete(id):
    cod = Config.delete(id)
    sms=""
    if(cod==400):
        sms={"error":"no se pudo borrar la configuración por que no existe"}
    else:
        sms= {"mensaje":"configuración eliminada correctamente"}
    return jsonify(sms),cod

