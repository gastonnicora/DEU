from flask import jsonify,  request, abort
from app.models.ejercicio import Ejercicio
from app.helpers.Serializacion import Serializacion
from app.helpers.Serializacion_ejercicio import Serializacion_Ejercicio
import json

def create():
    eje= Ejercicio.create(request.get_json())
    if eje is None:
         return jsonify({"error":"no se pudo guardar el ejercicio"}),400
    return jsonify(eje.toJSON()),200

def index():
    ejercicios= Serializacion.dump(Ejercicio.all(),nombre="Ejercicios",many=True)
    return jsonify(ejercicios),200

def get(id): 
    ejercicio= Ejercicio.get(id)
    if ejercicio is None:
        return jsonify({"error":"El ejercicio no existe"}),400
    return jsonify(Serializacion_Ejercicio.dump(ejercicio)),200

def get_by_entrenador(id): 
    ejercicio= Ejercicio.getbyEntrenador(id)
    if ejercicio is None:
        return jsonify({"error":"El entrenador no existe"}),400
    return jsonify(Serializacion_Ejercicio.dump_varios(ejercicio)),200

def update():
    eje=Ejercicio.update(request.get_json())
    if eje is None:
         return jsonify({"error":"No se pudo editar el ejercicio"}),400
    return jsonify(eje.toJSON()),200

def delete(id):
    cod= Ejercicio.delete(id)
    sms=""
    if(cod==400):
        sms={"error":"no se pudo borrar el ejercicio por que no existe"}
    else:
        sms= {"mensaje":"Ejercicio eliminado correctamente"}
    return jsonify(sms),cod

