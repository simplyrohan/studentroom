from flask import *
from utils import get_user, login_required

dashboard_bp = Blueprint("dashboard", __name__, url_prefix="/dashboard")

@dashboard_bp.route("/")
@login_required
def home():
    user = get_user(session["user"])
    return render_template("dashboard.html", user=user)