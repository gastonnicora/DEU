from app.models.modelos import db, Notificacion as n
from app.models.modelos_planos import Notificacion as N
from datetime import datetime



class Notificacion(object):
    
    @classmethod
    def create(cls,data):
        notificacion= n(
                entrenador= data.get("entrenador"),
                contenido= data.get("contenido"),
                fecha=datetime.now()
            )
        db.session.add(notificacion)
        db.session.commit()
        vi=N(notificacion)
        db.session.close()
        return vi
    
    @classmethod
    def all(cls):
        noti=n.query.filter_by(borrado=0).all()  
        db.session.close()
        return noti
    
    @classmethod
    def get(cls,id):
        noti= n.query.filter_by(borrado=0,id=id).first()
        db.session.close()
        return noti
    
    @classmethod
    def get_entrenador(cls,id):
        noti= n.query.filter_by(borrado=0,entrenador=id).all()
        db.session.close()
        return noti
    
    @classmethod
    def update(cls,data):
        noti= cls.get(data.get("id"))
        if noti is None:
            return None
        noti.entrenador= data.get("entrenador")
        noti.contenido= data.get("contenido")
        db.session.merge(noti)
        db.session.commit()
        vi=N(noti)
        db.session.close()
        return vi
        
    @classmethod
    def delete(cls,id):
        noti = cls.get(id)
        if noti is None:
            return 400
        noti.borrado=1
        db.session.merge(noti)
        db.session.commit()
        db.session.close()
        return 200
    
    @classmethod
    def get_in_list(cls,list):
        noti = db.session.query(n).filter(n.id.in_(list),n.borrado==0).all()
        return noti