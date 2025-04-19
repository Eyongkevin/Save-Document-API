from flask import jsonify
from flask_restx import Resource

from src.apps.user.parsers import api_namespace


@api_namespace.route("/ping/")
class PinPong(Resource):
    @api_namespace.doc("pin_users")
    def get(self):
        return jsonify({"status": "200 Ok", "message": "pong!"})
