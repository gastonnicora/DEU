from flask import jsonify,  request, abort
from app.models.ent_eje import Ent_eje
from app.helpers.Serializacion import Serializacion
import json

def create():
    e= Ent_eje.create(json.loads(request.get_json()))
    if e is None:
        return jsonify({"error":"no se pudo guardar la relación entrenamiento ejercicio"}),400
    return jsonify(e.toJSON()),200

def index():
    users= Serializacion.dump(Ent_eje.all(),nombre="Ent_ejes",many=True)
    return jsonify(users),200

def get(id): 
    user= Ent_eje.get(id)
    if user is None:
     return jsonify({"error":" la relación entrenamiento ejercicio no existe"}),400
    return jsonify(Serializacion.dump(user)) 

def update():
    e= Ent_eje.update(json.loads(request.get_json()))
    if e is None:
        return jsonify({"error":"no se pudo guardar la relación entrenamiento ejercicio"}),400
    return jsonify(e.toJSON()),200

def delete(id):
    cod=Ent_eje.delete(id)
    sms=""
    if(cod==400):
        sms={"error":"no se pudo borrar la relación entrenamiento ejercicio por que no existe"}
    else:
        sms= {"mensaje":"relación entrenamiento ejercicio eliminada correctamente"}
    return jsonify(sms),cod

