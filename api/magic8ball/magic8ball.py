from flask import Blueprint, render_template, request
from random import choice

magic8ball_bp = Blueprint("magic8ball", __name__, template_folder="templates")


class Magic8Ball:
    def __init__(self):
        self.answers = [
            "It is certain",
            "It is decidedly so",
            "Without a doubt",
            "Yes, definitely",
            "You may rely on it",
            "As I see it, yes",
            "Most likely",
            "Outlook good",
            "Yes",
            "Signs point to yes",
            "Reply hazy try again",
            "Ask again later",
            "Better not tell you now",
            "Cannot predict now",
            "Concentrate and ask again",
            "My reply is no",
            "My sources say no",
            "Outlook not so good",
            "Very doubtful"
        ]

    def shake(self):
        return choice(self.answers)

    def ask(self, question):
        return f"Question: {question}\n\nAnswer: {self.shake()}"


@magic8ball_bp.route("/", methods=["GET", "POST"])
def magic8ball_home():
    magic8ball_website = Magic8Ball()
    if request.method == "POST":
        question = request.form.get("question")
        answer = magic8ball_website.ask(question)
        return render_template("magic8ballanswer.html", question=question, answer=answer)
    return render_template("thirty_days.html")
