 
UPLOAD_FOLDER = './app/static/videos'
ALLOWED_EXTENSIONS = set(['mp4',"gif"])
 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

