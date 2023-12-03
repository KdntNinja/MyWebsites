from flask import Blueprint, render_template, request, redirect, url_for, send_from_directory, flash
from werkzeug.utils import secure_filename
from Crypto.Random import get_random_bytes
from werkzeug.exceptions import NotFound
import os

file_upload_bp = Blueprint("file_upload", __name__, template_folder="templates")

MAX_FILE_SIZE = 1 * 1024 * 1024  # 1MB
KEY = get_random_bytes(16)

current_dir = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(current_dir, "Data")
ALLOWED_EXTENSIONS = {
    "txt", "pdf", "png", "jpg", "jpeg", "gif", "py", "docx", "xlsx", "c", "cpp", "h", "hpp", "java", "class", "jar",
    "sln", "cs", "bat", "sh", "php", "html", "htm", "xhtml", "jhtml", "pl", "pm", "t", "pod", "m", "swift", "go", "py",
    "pyc", "pyo", "pyd", "rb", "java", "class", "jar", "rs", "dart", "kt", "kts", "ktm", "ktr", "clj", "cls", "cljc",
    "groovy", "gvy", "gy", "gsh", "lua", "r", "rnw", "rmd", "R", "Rprofile", "Rhistory", "Rdata", "Rd", "rsx", "pl",
    "pm", "xs", "t", "pod", "m", "f", "for", "f90", "f95", "f03", "f08", "f15", "f18", "s", "asm", "h", "hh", "hpp",
    "hxx", "c", "cc", "cpp", "cxx", "cob", "cbl", "cpy", "ads", "adb", "ml", "mli", "fs", "fsi", "fsx", "fst", "lisp",
    "lsp", "el", "cl", "mud", "l", "lua", "wl", "nb", "wls", "nbp", "kt", "kts", "scala", "sc", "java", "class", "jar",
    "sbt", "js", "jsx", "ts", "tsx", "html", "htm", "xhtml", "vue", "css", "less", "scss", "sass", "styl", "csv", "ics",
    "h", "hh", "hpp", "hxx", "c", "cc", "cpp", "cxx", "m", "markdown", "md", "mkd", "mkdn", "mdwn", "mdown", "ronn",
    "workbook"
}


@file_upload_bp.route("/Data", methods=["GET"])
def list_files():
    files = os.listdir(UPLOAD_FOLDER)
    return render_template("view_files.html", files=files)


@file_upload_bp.route("/Data/<filename>")
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)


@file_upload_bp.route("/Data/<filename>/key")
def file_key():
    return f"<br>Key: {KEY}"


def allowed_file(filename):
    return "." in filename and \
        filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@file_upload_bp.route("/Data/<filename>", methods=["POST"])
def delete_file(filename):
    if "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS:
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        if os.path.exists(file_path):
            os.remove(file_path)
            flash("File successfully deleted", "success")
            return redirect(url_for("file_upload.list_files"))
        else:
            raise NotFound("File not found")
    else:
        return "Invalid file", 400


@file_upload_bp.route("/", methods=["GET", "POST"])
def upload_file():
    files = os.listdir(UPLOAD_FOLDER)
    if request.method == "POST":
        if "file" not in request.files:
            return redirect(request.url)
        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)
        if file and allowed_file(file.filename):
            if file.content_length > MAX_FILE_SIZE:
                return "File size exceeds the limit of 1MB", 400
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
    return render_template("upload.html", max_file_size=MAX_FILE_SIZE / 1024 / 1024, files=files)


@file_upload_bp.route("/Data/<filename>")
def view_file(filename):
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            content = file.read()
        return render_template("view_file.html", content=content, filename=filename)
    else:
        raise NotFound("File not found")
