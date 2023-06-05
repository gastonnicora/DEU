from flask import jsonify,  request, abort
from app.models.video import Video
from app.helpers.Serializacion import Serializacion
import json

def create():
    video=Video.create(json.loads(request.get_json()))
    if video is None:
        return jsonify({"error":"no se pudo guardar el video"}),400
    return jsonify(video.toJSON()),200

def index():
    videos= Serializacion.dump(Video.all(),nombre="Videos",many=True)
    return jsonify(videos),200

def get(id): 
    video= Serializacion.dump(Video.get(id))
    return jsonify(video)

def update():
    video=Video.update(json.loads(request.get_json()))
    if video is None:
        return jsonify({"error":"no se pudo editar el video"}),400
    return jsonify(video.toJSON()),200

def delete(id):
    cod=Video.delete(id)
    sms=""
    if cod==400:
        sms={"error":"no se pudo borrar el video"}
    else:
        sms= {"mensaje":"Ejercicio eliminado correctamente"}
    return jsonify(sms),cod

