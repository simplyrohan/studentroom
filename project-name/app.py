from flask import *

# Blueprints
from auth import auth_bp
from dashboard import dashboard_bp

import secrets

app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(16)


@app.route("/")
def index():
    return render_template("index.html")

# Registering the blueprint
app.register_blueprint(auth_bp)
app.register_blueprint(dashboard_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
