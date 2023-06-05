from app.models.modelos import db, Video as v
from app.models.modelos_planos import Video as V

class Video(object):
    
    @classmethod
    def create(cls,data):
        video= v(
                nombre= data.get("nombre"), 
          
        )
        db.session.add(video)
        db.session.commit()
        vi=V(video)
        db.session.close()
        return vi
    
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
        if video is None:
            return None
        video.nombre= data.get("nombre")
        db.session.merge(video)
        db.session.commit()
        vi=V(video)
        db.session.close()
        return vi
        
    @classmethod
    def delete(cls,id):
        video = cls.get(id)
        if video is None:
            return 400
        db.session.delete(video)
        db.session.commit()
        db.session.close()
        return 200