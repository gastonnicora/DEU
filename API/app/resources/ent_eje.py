from flask import jsonify,  request, abort
from app.models.ent_eje import Ent_eje
from app.helpers.Serializacion import Serializacion

def create():
    Ent_eje.create(request.get_json())
    return jsonify(),200

def index():
    users= Serializacion.dump(Ent_eje.all(),nombre="Ent_ejes",many=True)
    return jsonify(users),200

def get(id): 
    user= Serializacion.dump(Ent_eje.get(id))
    return jsonify(user)

def update():
    Ent_eje.update(request.get_json())
    return jsonify(),200

def delete(id):
    Ent_eje.delete(id)
    return jsonify(),200

