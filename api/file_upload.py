from werkzeug.utils import secure_filename
from Crypto.Random import get_random_bytes
import os

MAX_FILE_SIZE = 1 * 1024 * 1024  # 1MB
KEY = get_random_bytes(16)

current_dir = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(current_dir, "Data")
ALLOWED_EXTENSIONS = {...}  # keep your existing extensions


def allowed_file(filename):
    return "." in filename and \
        filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def handle_request(request, response):
    if request.method == "POST":
        if "file" not in request.files:
            return response.redirect(request.url)
        file = request.files["file"]
        if file.filename == "":
            return response.redirect(request.url)
        if file and allowed_file(file.filename):
            if file.content_length > MAX_FILE_SIZE:
                return "File size exceeds the limit of 1MB", 400
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
    else:
        files = os.listdir(UPLOAD_FOLDER)
        return response.sendFile("/public/upload.html", files=files)
