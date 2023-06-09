from flask import jsonify,  request, abort
from app.models.entrenador_alumno import Entrenador_alumno
from app.helpers.Serializacion import Serializacion
import json

def create():
    ent=Entrenador_alumno.create(request.get_json())
    if ent is None:
        return jsonify({"error":"no se pudo guardar la relación entrenador alumno"}),400
    return jsonify(ent.toJSON()),200

def index():
    users= Serializacion.dump(Entrenador_alumno.all(),nombre="Entrenadores_alumnos",many=True)
    return jsonify(users),200

def get(id): 
    user= Entrenador_alumno.get(id)
    if user is None:
         return jsonify({"error":"no existe la relación entrenador alumno"}),400
    return jsonify(Serializacion.dump(user))

def update():
    ent= Entrenador_alumno.update(request.get_json())
    if ent is None:
        return jsonify({"error":"no se pudo editar la relación entrenador alumno"}),400
    return jsonify(ent.toJSON()),200

def delete(id):
    cod=Entrenador_alumno.delete(id)
    sms=""
    if(cod==400):
        sms={"error":"no se pudo borrar la relación entrenador alumno  por que no existe"}
    else:
        sms= {"mensaje":"relación entrenador alumno eliminada correctamente"}
    return jsonify(sms),cod
