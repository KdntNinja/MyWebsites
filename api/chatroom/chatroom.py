from datetime import datetime
from flask import Blueprint, redirect, render_template, request, session, url_for

chat_room_bp = Blueprint('chat_room_bp', __name__, template_folder='templates')

messages = []


def add_message(username, message):
    now = datetime.now().strftime("%H:%M:%S")  # new variable = now

    messages.append({"timestamp": now, "from": username, "message": message})


@chat_room_bp.route('/', methods=["GET", "POST"])  # route decorator that aligns to chat_index.html
def index():
    if request.method == "POST":
        session["username"] = request.form["username"]

    if "username" in session:
        return redirect(url_for("chat_room_bp.user", username=session["username"]))

    return render_template("chat_index.html")  # 'chat_index.html' now replaces message


@chat_room_bp.route('/chat/<username>', methods=["GET", "POST"])
def user(username):
    if request.method == "POST":
        username = session["username"]
        message = request.form["message"]
        add_message(username, message)
        return redirect(url_for("chat_room_bp.user", username=session["username"]))

    return render_template("chat.html", username=username, chat_messages=messages)
