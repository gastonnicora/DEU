from app.models.modelos import db, Video as v

class Video(object):
    
    @classmethod
    def create(cls,data):
        video= v(
                nombre= data.get("nombre"), 
          
        )
        db.session.add(video)
        db.session.commit()
        db.session.close()
    
    @classmethod
    def all(cls):
        video=v.query.filter_by().all()  
        db.session.close()
        return video
    
    @classmethod
    def get(cls,id):
        video= v.query.filter_by(id=id).first()
        db.session.close()
        return video
    
    @classmethod
    def update(cls,data):
        video= cls.get(data.get("id"))
        video.nombre= data.get("nombre"), 
        db.session.commit()
        db.session.close()
        
    @classmethod
    def delete(cls,id):
        video = cls.get(id)
        db.session.delete(video)
        db.session.commit()
        db.session.close()