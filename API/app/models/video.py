from app.models.modelos import db, Video as v
from app.models.modelos_planos import Video as V
from app.helpers.funciones_video import *
import os
import uuid



class Video(object):
    
    @classmethod
    def create(cls,data):
        # check if the post request has the file part
        if 'video' not in data.files:
            return "No se cargo un video para guardar"
        file = data.files['video']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            return "No se cargo un video para guardar"
        
        filename = str(uuid.uuid4())+".mp4"
        if file and allowed_file(file.filename):
            file.save(os.path.normpath(UPLOAD_FOLDER+"/"+filename))
        else:
            return "El video debe ser en formato MP4"
        video= v(
                nombre= filename, 
          
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
    