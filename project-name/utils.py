from flask import *
import dbclient
import uuid
from functools import wraps

db = dbclient.Collection("db")


def verifyuser(username, password):
    quer = db["users"].query(lambda x: x["username"] == username)
    if quer:
        if quer[0]["password"] == password:
            session["user"] = quer[0]["id"]
            return redirect(url_for("dashboard.home"))

        else:
            flash("Incorrect username or password")
            return redirect(url_for("auth.signin"))
    else:
        flash("Incorrect username or password")
        return redirect(url_for("auth.signin"))


def register(username, password):
    quer = db["users"].query(lambda x: x["username"] == username)
    if quer:
        flash("Username already taken")
        return redirect(url_for("auth.signup"))

    uid = uuid.uuid4().hex
    db["users"][uid] = {
        "id": uid,
        "username": username,
        "password": password,
        "profile": {
            "picture": "guest.svg",
            "name": username,
        },
    }
    session["user"] = uid
    return redirect(url_for("dashboard.home"))


def get_user(uid):
    quer = db["users"].query(lambda x: x["id"] == uid)
    if quer:
        return quer[0]
    else:
        return None


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user" not in session:
            return redirect(url_for("auth.signup"))

        return f(*args, **kwargs)

    return decorated_function
