from app.models.modelos import db, Ent_eje as e 
from app.models.modelos_planos import Ent_eje as E
from app.models.ejercicio import Ejercicio

class Ent_eje(object):
    
    @classmethod
    def create(cls,data):
        ent_eje= e(
                ent= data.get("ent"),
                eje= data.get("eje"),   
        )
        db.session.add(ent_eje)
        db.session.commit()
        ent= E(ent_eje)
        db.session.close()
        return ent
    
    @classmethod
    def all(cls):
        ent_eje=e.query.filter_by().all()  
        db.session.close()
        return ent_eje
    
    @classmethod
    def get(cls,id):
        ent_eje= e.query.filter_by(id=id).first()
        db.session.close()
        return ent_eje
    
    @classmethod
    def update(cls,data):
        ent_eje= cls.get(data.get("id"))
        if ent_eje is None:
            return None
        ent_eje.ent= data.get("ent")
        ent_eje.eje= data.get("eje")
        db.session.merge(ent_eje)
        db.session.commit()
        ent= E(ent_eje)
        db.session.close()
        return ent
        
    @classmethod
    def delete(cls,id):
        ent_eje = cls.get(id)
        if ent_eje is None:
            return 400
        db.session.delete(ent_eje)
        db.session.commit()
        db.session.close()
        return 200
        
    @classmethod
    def get_ejercicios_by_entrenamiento(cls,entrenamiento):
        eje=e.query.filter_by(ent= entrenamiento).all()
        list=[]
        for elem in eje:
            list.append(elem.eje)
        ejercicios= Ejercicio.get_in_list(list)
        return ejercicios