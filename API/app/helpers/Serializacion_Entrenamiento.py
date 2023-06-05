from app.helpers.Serializacion import Serializacion 
from app.helpers.Serializacion_ejercicio import Serializacion_Ejercicio
from app.models.ent_eje import Ent_eje
from app.models.ent_alu import Ent_alu

class Serializacion_Entrenamiento():
    
    @classmethod
    def dump(cls, entrenamiento):
       entrenamiento= Serializacion._serialize(entrenamiento)
       eje= Ent_eje.get_ejercicios(entrenamiento.get("id"))
       entrenamiento["Ejercicios"]= [Serializacion_Ejercicio.dump(elem) for elem in eje ]
       entrenamiento["Alumnos"]= [Serializacion.dump(elem) for elem in Ent_alu.get_alumnos(entrenamiento.get("id"))]
       return entrenamiento
        
    