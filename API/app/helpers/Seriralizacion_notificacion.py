from app.helpers.Serializacion import Serializacion 
from app.models.usuario import Usuario
from app.models.notificacion_alumno import Notificacion_alumno

class Serializacion_Notificacion():
    
    @classmethod
    def dump(cls, notificacion):
       notificacion= Serializacion._serialize(notificacion)
       list=[]
       for elem in Notificacion_alumno.get_notificacion(notificacion.get("id")):
           alu={"nombre":"", "apellido":"","visto":0}
           a= Usuario.get(elem.alumno)
           alu["nombre"]= a.nombre
           alu["apellido"]= a.apellido
           alu["visto"]= elem.visto
           list.append(alu)
       notificacion["Alumnos"]=list
       return notificacion
    
    @classmethod
    def dump_varios(cls, notificacion):
        return {
            "Total": len(notificacion),
            "Notificaciones": [cls.dump(elem) for elem in notificacion]
        }
    