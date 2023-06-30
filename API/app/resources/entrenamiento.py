from flask import jsonify,  request, abort
from app.models.entrenamiento import Entrenamiento
from app.helpers.Serializacion import Serializacion
from app.helpers.Serializacion_Entrenamiento import Serializacion_Entrenamiento
from app.models.ent_alu import Ent_alu
from app.models.ent_eje import Ent_eje
def create():
    ent=Entrenamiento.create(request.get_json())
    if ent is None:
         return jsonify({"error":"no se pudo guardar el entrenamiento"}),400
    [Ent_alu.create({"alu":alu,"ent":ent.id}) for alu in request.get_json().get("alu")]
    [Ent_eje.create({"eje":eje,"ent":ent.id}) for eje in request.get_json().get("eje")]
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
    ent= Entrenamiento.update(request.get_json())
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

def get_by_entrenador(id): 
    entrenamiento= Entrenamiento.get_by_entrenador(id)
    if entrenamiento is None:
        return jsonify({"error":"El entrenador no existe"}),400
    return jsonify(Serializacion_Entrenamiento.dump_varios(entrenamiento)),200

def get_entrenamientos_by_alumno(id): 
    entrenamiento= Ent_alu.get_entrenamiento_by_alumno(id)
    if entrenamiento is None:
        return jsonify({"error":"El alumno no existe"}),400
    return jsonify(Serializacion_Entrenamiento.dump_varios(entrenamiento)),200


