from flask import Blueprint, jsonify

user = Blueprint("user", __name__)


@user.route("/users/ping")
def ping_pong():
    return jsonify({"status": "200 Ok", "message": "pong!"})
