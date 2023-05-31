from flask import jsonify,  request, abort
from app.models.entrenamiento import Entrenamiento
from app.helpers.Serializacion import Serializacion
from app.helpers.Serializacion_Entrenamiento import Serializacion_Entrenamiento

def create():
    Entrenamiento.create(request.get_json())
    return jsonify(),200

def index():
    entrenamiento= Serializacion.dump(Entrenamiento.all(),nombre="Entrenamientos",many=True)
    return jsonify(entrenamiento),200

def get(id): 
    entrenamiento= Serializacion_Entrenamiento.dump(Entrenamiento.get(id))
    return jsonify(entrenamiento)

def update():
    Entrenamiento.update(request.get_json())
    return jsonify(),200

def delete(id):
    Entrenamiento.delete(id)
    return jsonify(),200


