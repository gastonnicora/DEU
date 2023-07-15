from app.models.modelos import db, Notificacion_alumno as n
from app.models.modelos_planos import Notificacion_alumno as N
from app.models.notificacion import Notificacion
from app.helpers.Serializacion import Serializacion 
from app.models.usuario import Usuario



class Notificacion_alumno(object):
    
    @classmethod
    def create(cls,data):
        notificacion= n(
            alumno=data.get("alumno"),
            notificacion= data.get("notificacion")
        )
        db.session.add(notificacion)
        db.session.commit()
        vi=N(notificacion)
        db.session.close()
        return vi
    
    @classmethod
    def all(cls):
        noti=n.query.filter_by().all()  
        db.session.close()
        return noti
    
    @classmethod
    def get(cls,id):
        noti= n.query.filter_by(id=id).first()
        db.session.close()
        return noti
    
    @classmethod
    def get_alumno(cls,id):
        noti= n.query.filter_by(alumno=id).all()
        list=[]
        for elem in noti:
            no=Serializacion._serialize(Notificacion.get(elem.notificacion))
            no["visto"]=elem.visto
            no["alumno"]=elem.alumno
            no["entrenador"]= Serializacion._serialize(Usuario.get(no["entrenador"]))
            list.append(no)
        db.session.close()
        return list
    
    @classmethod
    def get_alumno_notificacion(cls,id,noti):
        noo= n.query.filter_by(alumno=id,notificacion=noti).first()
        no=Serializacion.dump(Notificacion.get(noti))
        no["visto"]=noo.visto
        no["alumno"]=noo.alumno
        no["entrenador"]= Serializacion.dump(Usuario.get(no["entrenador"]))
        db.session.close()
        return no
    
    @classmethod
    def get_notificacion(cls,id):
        noti= n.query.filter_by(notificacion=id).all()
        db.session.close()
        return noti
    
    @classmethod
    def update(cls,data):
        noti= cls.get(data.get("id"))
        if noti is None:
            return None
        noti.alumno=data.get("alumno")
        noti.notificacion= data.get("notificacion")
        noti.visto= data.get("visto")
        db.session.merge(noti)
        db.session.commit()
        vi=N(noti)
        db.session.close()
        return vi
    
    @classmethod
    def leer(cls,data):
        noti= n.query.filter_by(alumno=data.get("alumno"), notificacion=data.get("id")).first()
        if noti is None:
            return None
        noti.visto=data.get("visto")
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
        db.session.delete(noti)
        db.session.commit()
        db.session.close()
        return 200
    
    @classmethod
    def delete_notificacion(cls,id):
        noti = cls.get_notificacion(id)
        if noti is None:
            return 400
        for elem in noti:
            db.session.delete(elem)
        db.session.commit()
        db.session.close()
        return 200
    
    @classmethod
    def get_in_list(cls,list):
        noti = db.session.query(n).filter(n.id.in_(list),n.borrado==0).all()
        return noti