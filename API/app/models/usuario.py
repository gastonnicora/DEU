from app.models.modelos import db, Usuario as u

class Usuario(object):
    
    @classmethod
    def create(cls,data):
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
        db.session.close()
    
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
        user.nombre= data.get("nombre"),
        user.apellido= data.get("apellido"),
        user.email= data.get("email"),
        user.contra = data.get("contra"), 
        user.tipo= data.get("tipo"), 
        user.posicion= data.get("posicion")
        db.session.commit()
        db.session.close()
        
    @classmethod
    def delete(cls,id):
        usuario = cls.get(id)
        usuario.borrado=1
        db.session.commit()
        db.session.close()
     
    @classmethod
    def get_in_list(cls,list):
        usuarios = db.session.query(u).filter(u.id.in_(list),u.borrado==0).all()
        return usuarios 
    
    @classmethod
    def login(cls,data):
        usuario = u.query.filter_by(email= data.get("email"),contra=data.get("contra"),borrado=0).first()
        db.session.close()
        return usuario