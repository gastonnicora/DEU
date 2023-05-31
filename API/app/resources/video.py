from flask import jsonify,  request, abort
from app.models.video import Video
from app.helpers.Serializacion import Serializacion

def create():
    Video.create(request.get_json())
    return jsonify(),200

def index():
    videos= Serializacion.dump(Video.all(),nombre="Videos",many=True)
    return jsonify(videos),200

def get(id): 
    video= Serializacion.dump(Video.get(id))
    return jsonify(video)

def update():
    Video.update(request.get_json())
    return jsonify(),200

def delete(id):
    Video.delete(id)
    return jsonify(),200

