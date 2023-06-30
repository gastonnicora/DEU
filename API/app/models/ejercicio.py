from app.models.modelos import db, Ejercicio as e
from app.models.modelos_planos import Ejercicio as E

class Ejercicio(object):
    
    @classmethod
    def create(cls,data): 
        eje= e(
                nombre= data.get("nombre"), 
                descripcion= data.get("descripcion"),
                tiempo= data.get("tiempo"),
                tipo_tiempo = data.get("tipo_tiempo"), 
                tipo= data.get("tipo"), 
                repeticiones= data.get("repeticiones"), 
                categoria= data.get("categoria"), 
                video= data.get("video"),
                publico= data.get("publico"),
                entrenador= data.get("entrenador")
            )
        db.session.add(eje)
        db.session.commit()
        ejercicio= E(eje)
        
        db.session.close()
        return ejercicio
    
    @classmethod
    def all(cls):
        eje=e.query.filter_by(borrado=0).all()  
        db.session.close()
        return eje
    
    @classmethod
    def get(cls,id):
        eje= e.query.filter_by(id=id,borrado=0).first()
        db.session.close()
        return eje
    
    @classmethod
    def update(cls,data):
        eje= cls.get(data.get("id"))
        if eje is None:
            return None
        eje.nombre= data.get("nombre") 
        eje.descripcion= data.get("descripcion")
        eje.tiempo= data.get("tiempo")
        eje.tipo_tiempo = data.get("tipo_tiempo") 
        eje.tipo= data.get("tipo")
        eje.repeticiones= data.get("repeticiones")
        eje.categoria= data.get("categoria")
        eje.video= data.get("video")
        eje.publico= data.get("publico")
        eje.entrenador= data.get("entrenador")
        db.session.merge(eje)
        db.session.commit()
        ejer= E(eje)
        db.session.close()
        return ejer
        
    @classmethod
    def delete(cls,id): 
        eje = cls.get(id)
        if eje is None:
            return 400
        eje.borrado=1
        db.session.merge(eje)
        db.session.commit()
        db.session.close()
        return 200
    
    @classmethod
    def get_in_list(cls,list):
        ejercicios = db.session.query(e).filter(e.id.in_(list),e.borrado==0).all() 
        return ejercicios
    
    @classmethod
    def getbyEntrenador(cls,id):
        eje=e.query.filter_by(borrado=0,entrenador=id).all()  
        db.session.close()
        return eje