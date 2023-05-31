from flask import jsonify,  request, abort
from app.models.usuario import Usuario
from app.helpers.Serializacion import Serializacion
from app.models.entrenador_alumno import Entrenador_alumno

def create():
    Usuario.create(request.get_json())
    return jsonify(),200

def index():
    users= Serializacion.dump(Usuario.all(),nombre="Usuarios",many=True)
    return jsonify(users),200

def get(id): 
    user= Serializacion.dump(Usuario.get(id))
    return jsonify(user)

def update():
    Usuario.update(request.get_json())
    return jsonify(),200

def delete(id):
    Usuario.delete(id)
    return jsonify(),200

def get_alumnos(id):
    alumnos = Serializacion.dump( Entrenador_alumno.get_alum_by_entrenador(id),nombre="Alumnos",many=True)
    return jsonify(alumnos)

def login(): 
    user= Serializacion.dump(Usuario.login(request.get_json()))
    return jsonify(user)