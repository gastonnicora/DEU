from app.models.modelos import db, Config as e

class Config(object):
    
    @classmethod
    def create(cls,data):
        config= e(
                us= data.get("us"),
                tema= data.get("tema"),
                fuente= data.get("fuente")
        )
        db.session.add(config)
        db.session.commit()
        db.session.close()
    
    @classmethod
    def all(cls):
        config=e.query.filter_by().all()  
        db.session.close()
        return config
    
    @classmethod
    def get(cls,id):
        config= e.query.filter_by(id=id).first()
        db.session.close()
        return config
    
    @classmethod
    def update(cls,data):
        config= cls.get(data.get("id"))
        config.us= data.get("us"),
        config.tema= data.get("tema"),
        config.fuente= data.get("fuente")
        db.session.commit()
        db.session.close()
    
 
    @classmethod
    def delete(cls,id):
        config = cls.get(id)
        db.session.delete(config)
        db.session.commit()
        db.session.close()