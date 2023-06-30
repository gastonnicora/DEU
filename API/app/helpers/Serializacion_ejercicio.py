from app.helpers.Serializacion import Serializacion 
from app.models.video import Video

class Serializacion_Ejercicio():
    
    @classmethod
    def dump(cls, ejercicio):
        eje= Serializacion._serialize(ejercicio)
        eje["video"]= Serializacion._serialize(Video.get(ejercicio.video))
        return eje
   
    @classmethod
    def dump_varios(cls, ejercicio):
        eje={}
        eje["Ejercicios"]= [Serializacion_Ejercicio.dump(elem) for elem in ejercicio ]
        eje["Total"]=len(ejercicio)
        return eje

