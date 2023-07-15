from flask_socketio import SocketIO
from flask import  request
from flask_socketio import emit
from app.models.notificacion_alumno import Notificacion_alumno
import json

socketio = SocketIO( cors_allowed_origins='*')

users={}
@socketio.on('connect')
def test_connect(auth):
    emit('my_response', {'data': 'Connected'})

@socketio.on('disconnect')
def test_disconnect():
    users.pop(request.sid,'No user found')
    print('Client disconnected')
    print(users)
    
@socketio.on('coneccion')
def test_coneccion(data):
    users[request.sid] = data
    print(users)
    emit('coneccion')

def notificacion(data):
    
    print(data)
    for id in data["ids"]:
        print(id)
        for uuid in users:
            print("enviando notificaciones")
            print(users[uuid])
            print(users[uuid]==id)
            if users[uuid]==id:
                noti=Notificacion_alumno.get_alumno_notificacion(id,data["notificacion"])
                noti["fecha"]=noti["fecha"].strftime("%a, %d %b %Y %H:%M:%S GMT")
                print(id)
                socketio.emit('notificacion',noti, room=uuid)
            print("notificaciones enviadas") 