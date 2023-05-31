from app.helpers.Serializacion import Serializacion 
from app.models.video import Video

class Serializacion_Ejercicio():
    
    @classmethod
    def dump(cls, ejercicio):
        eje= Serializacion._serialize(ejercicio)
        eje["video"]= Serializacion._serialize(Video.get(ejercicio.video))
        return eje
   

