from app.models.modelos import db, Ent_alu as e
from app.models.usuario import Usuario

class Ent_alu(object):
    
    @classmethod
    def create(cls,data):
        ent_alu= e(
                ent= data.get("ent"),
                alu= data.get("alu")  
        )
        db.session.add(ent_alu)
        db.session.commit()
        db.session.close()
    
    @classmethod
    def all(cls):
        ent_alu=e.query.filter_by().all()  
        db.session.close()
        return ent_alu
    
    @classmethod
    def get(cls,id):
        ent_alu= e.query.filter_by(id=id).first()
        db.session.close()
        return ent_alu
    
    @classmethod
    def update(cls,data):
        ent_alu= cls.get(data.get("id"))
        ent_alu.ent= data.get("ent"),
        ent_alu.alu= data.get("alu")
        db.session.commit()
        db.session.close()
    
    @classmethod
    def update_alu(cls,data):
        ent_alu= cls.get(data.get("id"))
        ent_alu.coment_jug= data.get("coment_jug")
        db.session.commit()
        db.session.close()
    
    @classmethod
    def update_entrenador(cls,data):
        ent_alu= cls.get(data.get("id"))
        ent_alu.asistencia= data.get("asistencia")
        ent_alu.nota= data.get("nota")
        ent_alu.coment_ent= data.get("coment_ent")
        db.session.commit()
        db.session.close()
      
    @classmethod
    def delete(cls,id):
        ent_alu = cls.get(id)
        db.session.delete(ent_alu)
        db.session.commit()
        db.session.close()
        
    @classmethod
    def get_alumnos(cls,entrenamiento):
        
        user=e.query.filter_by(ent= entrenamiento).all()
        list=[]
        for elem in user:
            list.append(elem.id)
        users= Usuario.get_in_list(list)
        return users