from flask import jsonify,  request, abort
from app.models.ent_alu import Ent_alu
from app.helpers.Serializacion import Serializacion

def create():
    Ent_alu.create(request.get_json())
    return jsonify(),200

def index():
    users= Serializacion.dump(Ent_alu.all(),nombre="Ent_alus",many=True)
    return jsonify(users),200

def get(id): 
    user= Serializacion.dump(Ent_alu.get(id))
    return jsonify(user)

def update():
    Ent_alu.update(request.get_json())
    return jsonify(),200

def update_alu():
    Ent_alu.update_alu(request.get_json())
    return jsonify(),200

def update_entrenador():
    Ent_alu.update_entrenador(request.get_json())
    return jsonify(),200

def delete(id):
    Ent_alu.delete(id)
    return jsonify(),200

