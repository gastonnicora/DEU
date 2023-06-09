from flask import jsonify,  request, abort
from app.models.ent_alu import Ent_alu
from app.helpers.Serializacion import Serializacion
import json

def create():
    e=Ent_alu.create(request.get_json())
    if e is None:
        return jsonify({"error":"no se pudo guardar la relación entrenamiento alumno"}),400
    return jsonify(e.toJSON()),200

def index():
    users= Serializacion.dump(Ent_alu.all(),nombre="Ent_alus",many=True)
    return jsonify(users),200

def get(id): 
    user= Ent_alu.get(id)
    if user is None:
        return jsonify({"error":" la relación entrenamiento alumno no existe"}),400
    return jsonify(Serializacion.dump(user))

def update():
    e=Ent_alu.update(request.get_json())
    if e is None:
        return jsonify({"error":"no se pudo editar la relación entrenamiento alumno"}),400
    return jsonify(e.toJSON()),200

def update_alu():
    e= Ent_alu.update_alu(request.get_json())
    if e is None:
        return jsonify({"error":"no se pudo editar la relación entrenamiento alumno"}),400
    return jsonify(e.toJSON()),200

def update_entrenador():
    e= Ent_alu.update_entrenador(request.get_json())
    if e is None:
        return jsonify({"error":"no se pudo editar la relación entrenamiento alumno"}),400
    return jsonify(e.toJSON()),200

def delete(id):
    cod=Ent_alu.delete(id)
    sms=""
    if(cod==400):
        sms={"error":"no se pudo borrar la relación entrenamiento alumno por que no existe"}
    else:
        sms= {"mensaje":"relación entrenamiento alumno eliminada correctamente"}
    return jsonify(sms),cod

