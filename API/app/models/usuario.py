from app.models.modelos import db, Usuario as u
from app.models.modelos_planos import Usuario as U
from app.models.config import Config

class Usuario(object):
    
    @classmethod
    def create(cls,data):
        usu= cls.email(data.get("email"))
        if usu is not None:
            return 400
        user= u(
                nombre= data.get("nombre"), 
                apellido= data.get("apellido"),
                email= data.get("email"),
                contra = data.get("contra"), 
                tipo= data.get("tipo"), 
                posicion= data.get("posicion")
            )
        
        db.session.add(user)
        db.session.commit()
        usuario= U(user)
        Config.create({"us":usuario.id})
        db.session.close()
        return usuario
    
    @classmethod
    def all(cls):
        users=u.query.filter_by(borrado=0).all()  
        db.session.close()
        return users
    
    @classmethod
    def get(cls,id):
        user= u.query.filter_by(id=id,borrado=0).first()
        db.session.close()
        return user
    
    @classmethod
    def update(cls,data):
        user= cls.get(data.get("id"))
        if user is None:
            return None
        user.nombre= data.get("nombre")
        user.apellido= data.get("apellido")
        user.email= data.get("email")
        user.contra = data.get("contra") 
        user.tipo= data.get("tipo") 
        user.posicion= data.get("posicion") 
        db.session.merge(user)
        db.session.commit() 
        usuario= U(user)
        db.session.close()
        return usuario
    
        
    @classmethod
    def delete(cls,id):
        usuario = cls.get(id)
        if usuario is None:
            return 400
        usuario.borrado=1
        db.session.merge(usuario)
        db.session.commit()
        db.session.close()
        return 200
     
    @classmethod
    def get_in_list(cls,list):
        usuarios = db.session.query(u).filter(u.id.in_(list),u.borrado==0).all()
        return usuarios 
    
    @classmethod
    def not_in_list(cls,list):
        usuarios = db.session.query(u).filter(u.id.notin_(list),u.borrado==0,u.tipo==1).all()
        return usuarios 
    
    @classmethod
    def login(cls,data):
        usuario = u.query.filter_by(email= data.get("email"),contra=data.get("contra"),borrado=0).first()
        db.session.close()
        return usuario
    
    @classmethod
    def email(cls,email):
        usuario = u.query.filter_by(email=email, borrado=0).first()
        db.session.close()
        return usuario
    
    @classmethod
    def alumnos(cls):
        usuarios= u.query.filter_by(borrado= 0,tipo=1).all() 
        db.session.close()
        return usuarios
    
    @classmethod
    def update_pass(cls,data):
        user= cls.get(data.get("id"))
        sms=""
        if user is None:
            return {"error":"No se pudo editar la contraseña por que el id no existe"}
        if user.contra==data.get("contra"):
            if data.get("new_contra")==data.get("rp_contra"):
                user.contra = data.get("new_contra") 
                db.session.merge(user)
                db.session.commit() 
                db.session.close()
                sms="La contraseña se actualizo con exito"
            else:
                sms={"error":"Los campos Nueva contraseña y Repita la contraseña no coinciden"}
        else:
            sms={"error":"Error al ingresar la contraseña antigua"}
        return sms