from app.models.modelos import db, Ejercicio as e

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
                video= data.get("video")
            )
        db.session.add(eje)
        db.session.commit()
        db.session.close()
    
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
        eje.nombre= data.get("nombre"), 
        eje.descripcion= data.get("descripcion"),
        eje.tiempo= data.get("tiempo"),
        eje.tipo_tiempo = data.get("tipo_tiempo"), 
        eje.tipo= data.get("tipo"), 
        eje.repeticiones= data.get("repeticiones"), 
        eje.categoria= data.get("categoria"), 
        eje.video= data.get("video")
        db.session.commit()
        db.session.close()
        
    @classmethod
    def delete(cls,id):
        eje = cls.get(id)
        eje.borrado=1
        db.session.commit()
        db.session.close()
    
    @classmethod
    def get_in_list(cls,list):
        ejercicios = e.query.filter(e.id.in_(list),e.borrado==0).all()
        return ejercicios