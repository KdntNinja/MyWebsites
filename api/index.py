from flask import Flask
""", request, jsonify
from functools import wraps
from http import HTTPStatus"""
import secrets

from welcome_page.welcome_page import welcome_page_bp
from file_upload.file_upload import file_upload_bp
from magic8ball.magic8ball import magic8ball_bp
from chatroom.chatroom import chat_room_bp


"""def require_api_key(view_function):
    @wraps(view_function)
    def decorated_function(*args, **kwargs):
        try:
            api_key = request.headers.get('X-API-KEY')

            if not api_key:
                return jsonify({'error': 'Missing API key'}), HTTPStatus.UNAUTHORIZED

            if api_key != 'your-expected-api-key':
                return jsonify({'error': 'Invalid API key'}), HTTPStatus.UNAUTHORIZED

            return view_function(*args, **kwargs)
        except Exception as e:
            return jsonify({'error': str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR

    return decorated_function

"""
secret_key = secrets.token_hex(16)

app = Flask(__name__)
app.secret_key = secret_key

app.register_blueprint(welcome_page_bp)
app.register_blueprint(chat_room_bp, url_prefix="/chatroom")
app.register_blueprint(magic8ball_bp, url_prefix="/magic8ball")
app.register_blueprint(file_upload_bp, url_prefix="/file_upload")


@app.before_request
def before_request():
    pass


if __name__ == "__main__":
    app.run(debug=True)
