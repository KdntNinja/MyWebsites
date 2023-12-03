from flask import Flask
import secrets

from welcome_page.welcome_page import welcome_page_bp
from file_upload.file_upload import file_upload_bp
from magic8ball.magic8ball import magic8ball_bp
from chatroom.chatroom import chat_room_bp

secret_key = secrets.token_hex(16)

app = Flask(__name__)
app.secret_key = secret_key

app.register_blueprint(welcome_page_bp)
app.register_blueprint(chat_room_bp, url_prefix="/chatroom")
app.register_blueprint(magic8ball_bp, url_prefix="/magic8ball")
app.register_blueprint(file_upload_bp, url_prefix="/file_upload")

if __name__ == "__main__":
    app.run(debug=True)
