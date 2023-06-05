from flask import jsonify,  request, abort
from app.models.entrenamiento import Entrenamiento
from app.helpers.Serializacion import Serializacion
from app.helpers.Serializacion_Entrenamiento import Serializacion_Entrenamiento
import json

def create():
    ent=Entrenamiento.create(json.loads(request.get_json()))
    if ent is None:
         return jsonify({"error":"no se pudo guardar el entrenamiento"}),400
    return jsonify(ent.toJSON()),200

def index():
    entrenamiento= Serializacion.dump(Entrenamiento.all(),nombre="Entrenamientos",many=True)
    return jsonify(entrenamiento),200

def get(id): 
    entrenamiento= Entrenamiento.get(id)
    if entrenamiento is None:
        return jsonify({"error":"El entrenamiento no existe"}),400
    return jsonify(Serializacion_Entrenamiento.dump(entrenamiento)),200

def update():
    ent= Entrenamiento.update(json.loads(request.get_json()))
    if ent is None:
         return jsonify({"error":"no se pudo editar el entrenamiento"}),400
    return jsonify(ent.toJSON()),200

def delete(id):
    cod=Entrenamiento.delete(id)
    sms=""
    if(cod==400):
        sms={"error":"no se pudo borrar el entrenamiento por que no existe"}
    else:
        sms= {"mensaje":"entrenamiento eliminado correctamente"}
    return jsonify(sms),cod


