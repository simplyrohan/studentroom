from flask import *
from utils import register, verifyuser

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        # Handle the POST request
        return register(request.form["username"], request.form["password"])

    msgs = get_flashed_messages()
    return render_template("auth.html", signup=True, msgs=msgs)


@auth_bp.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        # Handle the POST request
        return verifyuser(request.form["username"], request.form["password"])
    msgs = get_flashed_messages()
    return render_template("auth.html", signup=False, msgs=msgs)
