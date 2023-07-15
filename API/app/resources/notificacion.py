from flask import jsonify,  request, abort
from app.models.notificacion import Notificacion
from app.models.notificacion_alumno import Notificacion_alumno
from app.helpers.Serializacion import Serializacion
from app.events import notificacion 

from app.helpers.Seriralizacion_notificacion import Serializacion_Notificacion

import json

def create():
    notificacio=Notificacion.create(request.get_json())
    if notificacio is None:
        return jsonify({"error":"no se pudo guardar el notificación"}),400
    alumnos= request.get_json().get("alumnos")
    for alumno in alumnos :
        no= Notificacion_alumno.create({"alumno":alumno,"notificacion":notificacio.id})
        if no is None:
            Notificacion_alumno.delete_notificacion(notificacio.id)
            Notificacion.delete(notificacio.id)
            return jsonify({"error":"no se pudo guardar el notificación"}),400
    notificacion({"ids":alumnos,"notificacion":notificacio.id})
    return jsonify(notificacio.toJSON()),200

def index():
    notificacions= Serializacion_Notificacion.dump_varios(Notificacion.all())
    return jsonify(notificacions),200

def get(id): 
    notificacion= Serializacion_Notificacion.dump(Notificacion.get(id))
    return jsonify(notificacion)

def get_entrenador(id): 
    notificacion= Serializacion_Notificacion.dump_varios(Notificacion.get_entrenador(id))
    return jsonify(notificacion)

def get_alumno(id): 
    notificaciones=Notificacion_alumno.get_alumno(id)
    return jsonify(notificaciones)

def update():
    notificacion=Notificacion.update(request.get_json())
    if notificacion is None:
        return jsonify({"error":"no se pudo editar el notificacion"}),400
    return jsonify(notificacion.toJSON()),200

def leer():
    notificacion=Notificacion_alumno.leer(request.get_json())
    if notificacion is None:
        return jsonify({"error":"no se pudo marcar como leida"}),400
    return jsonify(notificacion.toJSON()),200

def delete(id):
    cod=Notificacion.delete(id)
    sms=""
    if cod==400:
        sms={"error":"no se pudo borrar el notificacion"}
    else:
        sms= {"mensaje":"Ejercicio eliminado correctamente"}
    return jsonify(sms),cod

