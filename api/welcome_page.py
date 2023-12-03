from flask import Blueprint, render_template

welcome_page_bp = Blueprint("welcome_page", __name__, template_folder="templates")


@welcome_page_bp.route("/")
def home():
    return render_template("index.html")
