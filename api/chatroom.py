from datetime import datetime
from flask import request, session

messages = []


def add_message(username, message):
    now = datetime.now().strftime("%H:%M:%S")  # new variable = now
    messages.append({"timestamp": now, "from": username, "message": message})


def handle_request(request, response):
    if request.method == "POST":
        session["username"] = request.form["username"]

    if "username" in session:
        username = session["username"]
        message = request.form.get("message")
        if message:
            add_message(username, message)
        response.redirect(f"/chat/{username}")
    else:
        response.sendFile("/public/chat_index.html")

    return response
