from app.models.modelos import db, Entrenador_alumno as e
from  app.models.modelos_planos import Entrenador_alumno as E
from app.models.usuario import Usuario
class Entrenador_alumno(object):
    
    @classmethod
    def create(cls,data):
        entrenador_alumno= e(
                entrenador= data.get("entrenador"),
                alumno= data.get("alumno")
        )
        db.session.add(entrenador_alumno)
        db.session.commit()
        ent= E(entrenador_alumno)
        db.session.close()
        return ent
    
    @classmethod
    def all(cls):
        entrenador_alumno=e.query.filter_by().all()  
        db.session.close()
        return entrenador_alumno
    
    @classmethod
    def get(cls,id):
        entrenador_alumno= e.query.filter_by(id=id).first()
        db.session.close()
        return entrenador_alumno
    
    @classmethod
    def update(cls,data):
        entrenador_alumno= cls.get(data.get("id"))
        if entrenador_alumno is None:
            return None
        entrenador_alumno.entrenador= data.get("entrenador")
        entrenador_alumno.alumno= data.get("alumno")
        db.session.merge(entrenador_alumno)
        db.session.commit()
        ent= E(entrenador_alumno)
        db.session.close()
        return ent
    
 
    @classmethod
    def delete(cls,id):
        entrenador_alumno = cls.get(id)
        if entrenador_alumno is None:
            return 400
        db.session.delete(entrenador_alumno)
        db.session.commit()
        db.session.close()
        return 200
        
    @classmethod
    def get_alum_by_entrenador(cls,entrenador):
        alu=e.query.filter_by(entrenador= entrenador).all()
        list=[]
        for elem in alu:
            list.append(elem.alumno)
        alumnos=Usuario.get_in_list(list)
        return alumnos