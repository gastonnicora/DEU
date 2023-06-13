from flask import jsonify,  request, abort
from app.models.usuario import Usuario
from app.helpers.Serializacion import Serializacion
from app.models.entrenador_alumno import Entrenador_alumno
import json

def create(): 
    user=Usuario.create(request.get_json())
    if user is None:
        return jsonify({"error":"no se pudo guardar el usuario"}),400
    elif user == 400:
        return jsonify({"error":"no se pudo guardar el usuario por que ya existe uno con el mismo email"}),400
    return jsonify(user.toJSON()),200

def index():
    users= Serializacion.dump(Usuario.all(),nombre="Usuarios",many=True)
    return jsonify(users),200

def get(id): 
    usuario= Usuario.get(id)
    if(usuario != None):
        user= Serializacion.dump(usuario)
        return jsonify(user),200
    else:
        return jsonify({"error":"El usuario seleccionado no existe"}),400

def update():
    user=Usuario.update(request.get_json())
    if user is None:
        return jsonify({"error":"no se pudo editar el usuario"}),400
    return jsonify(user.toJSON()),200

def update_pass():
    user=Usuario.update_pass(request.get_json())
    return jsonify(user),200

def delete(id):
    cod= Usuario.delete(id)
    sms=""
    if(cod==400):
        sms={"error":"no se pudo borrar el usuario por que no existe"}
    else:
        sms= {"mensaje":"Usuario eliminado correctamente"}
    return jsonify(sms),cod

def get_alumnos(id):
    alumnos = Serializacion.dump( Entrenador_alumno.get_alum_by_entrenador(id),nombre="Alumnos",many=True)
    return jsonify(alumnos),200

def alumnos():
    alumnos = Serializacion.dump( Usuario.alumnos(),nombre="Alumnos",many=True)
    return jsonify(alumnos),200

def login(): 
    user= Usuario.login(request.get_json())
    if user is None:
         return jsonify({"error":"usuario o contraseña incorrecto"}),400
    return jsonify(Serializacion.dump(user)),200