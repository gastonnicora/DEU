from flask import jsonify,  request, abort
from app.models.entrenador_alumno import Entrenador_alumno
from app.helpers.Serializacion import Serializacion

def create():
    Entrenador_alumno.create(request.get_json())
    return jsonify(),200

def index():
    users= Serializacion.dump(Entrenador_alumno.all(),nombre="Entrenadores_alumnos",many=True)
    return jsonify(users),200

def get(id): 
    user= Serializacion.dump(Entrenador_alumno.get(id))
    return jsonify(user)

def update():
    Entrenador_alumno.update(request.get_json())
    return jsonify(),200

def delete(id):
    Entrenador_alumno.delete(id)
    return jsonify(),200

