from flask import jsonify,  request, abort
from app.models.ejercicio import Ejercicio
from app.helpers.Serializacion import Serializacion
from app.helpers.Serializacion_ejercicio import Serializacion_Ejercicio

def create():
    Ejercicio.create(request.get_json())
    return jsonify(),200

def index():
    ejercicios= Serializacion.dump(Ejercicio.all(),nombre="Ejercicios",many=True)
    return jsonify(ejercicios),200

def get(id): 
    ejercicio= Serializacion_Ejercicio.dump(Ejercicio.get(id))
    return jsonify(ejercicio)

def update():
    Ejercicio.update(request.get_json())
    return jsonify(),200

def delete(id):
    Ejercicio.delete(id)
    return jsonify(),200

