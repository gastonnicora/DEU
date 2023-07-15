from flask import jsonify,  request, abort
from app.models.notificacion_alumno import Notificacion_alumno
from app.helpers.Serializacion import Serializacion
import json

def create():
    n_a=Notificacion_alumno.create(request.get_json())
    if n_a is None:
        return jsonify({"error":"no se pudo guardar el n_a"}),400
    return jsonify(n_a.toJSON()),200

def index():
    n_as= Serializacion.dump(Notificacion_alumno.all(),nombre="Notificacion_alumnos",many=True)
    return jsonify(n_as),200

def get(id): 
    n_a= Serializacion.dump(Notificacion_alumno.get(id))
    return jsonify(n_a)

def update():
    n_a=Notificacion_alumno.update(request.files)
    if n_a is None:
        return jsonify({"error":"no se pudo editar el n_a"}),400
    return jsonify(n_a.toJSON()),200

def delete(id):
    cod=Notificacion_alumno.delete(id)
    sms=""
    if cod==400:
        sms={"error":"no se pudo borrar el n_a"}
    else:
        sms= {"mensaje":"Ejercicio eliminado correctamente"}
    return jsonify(sms),cod

