from app.models.modelos import db, Config as e
from app.models.modelos_planos import Config as E

class Config(object):
    
    @classmethod
    def create(cls,data):
        config= e(
                us= data.get("us"),
                tema= data.get("tema")
        )
        db.session.add(config)
        db.session.commit()
        c=  E(config)
        db.session.close()
        return c
    
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
        print(data)
        config= cls.get(data.get("id"))
        if config is None:
            return None
        config.us= data.get("us")
        config.tema= data.get("tema")
        db.session.merge(config)
        db.session.commit()
        c= E(config)
        db.session.close()
        return c
 
    @classmethod
    def delete(cls,id):
        config = cls.get(id)
        if config is None:
            return 400
        db.session.delete(config)
        db.session.commit()
        db.session.close()
        return 200
    
    @classmethod
    def getByUser(cls,id):
        config= e.query.filter_by(us=id).first()
        db.session.close()
        return config