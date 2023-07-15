
import json
class Usuario():
    def __init__(cls,data):
        cls.id=data.id
        cls.nombre= data.nombre
        cls.apellido=data.apellido
        cls.email=data.email
        cls.contra=data.contra
        cls.tipo=data.tipo
        cls.posicion= data.posicion
        cls.borrado = data.borrado
    def toJSON(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4))

class Ejercicio():
    def __init__(cls,data):
        cls.id=data.id
        cls.nombre= data.nombre
        cls.descripcion=data.descripcion
        cls.tiempo=data.tiempo
        cls.repeticiones=data.repeticiones
        cls.tipo=data.tipo
        cls.tipo_tiempo=data.tipo_tiempo
        cls.categoria= data.categoria
        cls.video= data.video
        cls.borrado = data.borrado
        cls.entrenador= data.entrenador
        cls.publico= data.publico
    def toJSON(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4))
        
class Video():
    def __init__(cls,data):
        cls.id=data.id
        cls.nombre= data.nombre
    def toJSON(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4))


class Entrenamiento():
    def __init__(cls,data):
        cls.id=data.id
        cls.nombre= data.nombre
        cls.descripcion=data.descripcion
        cls.fecha=data.fecha
        cls.entrenador= data.entrenador
        cls.borrado = data.borrado
        cls.tipo=data.tipo
    def toJSON(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4))

class Ent_eje():
    def __init__(cls,data):
        cls.id=data.id
        cls.eje= data.eje
        cls.ent=data.ent
        
    def toJSON(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4))
        
class Ent_alu():
    def __init__(cls,data):
        cls.id=data.id
        cls.ent= data.ent
        cls.alu=data.alu
        cls.coment_jug= data.coment_jug
        cls.asistencia= data.asistencia
        cls.nota= data.nota
        cls.coment_ent= data.coment_ent
        
    def toJSON(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4))

class Notificacion():
    def __init__(cls,data):
        cls.id=data.id
        cls.enentrenador= data.entrenador
        cls.contenido=data.contenido
        cls.borrado= data.borrado
        
    def toJSON(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4))
        
class Notificacion_alumno():
    def __init__(cls,data):
        cls.id=data.id
        cls.alumno= data.alumno
        cls.notificacion=data.notificacion
        cls.visto= data.visto
        
    def toJSON(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4))
        
class Config():
    def __init__(cls,data):
        cls.id=data.id
        cls.us=data.us
        cls.tema= data.tema
        
    def toJSON(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4))
        
class Entrenador_alumno():
    def __init__(cls,data):
        cls.id=data.id
        cls.alumno=data.alumno
        cls.entrenador= data.entrenador
        
    def toJSON(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4))
