from flask import Flask, jsonify

from src.utils import BASE_DIR

app = Flask(
    __name__,
    # set base template
    instance_path=str(BASE_DIR / "src" / "settings"),
    instance_relative_config=True,
)

app.config.from_object(__name__)
app.config.from_pyfile("dev.py")


# Testing
@app.route("/users/ping")
def ping_pong():
    return jsonify({"status": "success", "message": "pong!"})
