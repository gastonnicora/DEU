from app.models.modelos import db, Entrenamiento as e

class Entrenamiento(object):
    
    @classmethod
    def create(cls,data):
        entrenamiento= e(
                nombre= data.get("nombre"),
                descripcion= data.get("descripcion"),
                fecha= data.get("fecha"),
                entrenador= data.get("entrenador")
        )
        db.session.add(entrenamiento)
        db.session.commit()
        db.session.close()
    
    @classmethod
    def all(cls):
        entrenamiento=e.query.filter_by(borrado=0).all()  
        db.session.close()
        return entrenamiento
    
    @classmethod
    def get(cls,id):
        entrenamiento= e.query.filter_by(id=id,borrado=0).first()
        db.session.close()
        return entrenamiento
    
    @classmethod
    def update(cls,data):
        entrenamiento= cls.get(data.get("id"))
        entrenamiento.nombre= data.get("nombre"),
        entrenamiento.descripcion= data.get("descripcion"),
        entrenamiento.fecha= data.get("fecha"),
        entrenamiento.entrenador= data.get("entrenador") 
        db.session.commit()
        db.session.close()
        
    @classmethod
    def delete(cls,id):
        entrenamiento = cls.get(id)
        entrenamiento.borrado=1
        db.session.commit()
        db.session.close()
    