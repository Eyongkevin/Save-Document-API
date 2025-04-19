from flask import jsonify, make_response, request
from flask_restx import Resource

from src.apps import app
from src.apps.user import services, token_authentication
from src.apps.user.parsers import api_namespace, registration_parser
from src.apps.user.serializers import register_serializer


@api_namespace.route("/ping/")
class PinPong(Resource):
    @api_namespace.doc("pin_users")
    def get(self):
        return jsonify({"status": "200 Ok", "message": "pong!"})


@api_namespace.route("/auth/register/")
class Registration(Resource):
    @api_namespace.doc("auth_register")
    @api_namespace.expect(register_serializer)
    def post(self):
        """Register user"""

        try:
            user = services.register(
                api_namespace.payload["username"],
                api_namespace.payload["email"],
                api_namespace.payload["password"],
            )

            auth_token = token_authentication.generate_token_header(
                user.username, app.config["PRIVATE_KEY"]
            )

            responseObject = {
                "status": "success",
                "message": "Successfully registered",
                "auth_token": auth_token,
            }
            return make_response(jsonify(responseObject), 201)
        except PermissionError:
            responseObject = {
                "status": "fail",
                "message": "User already exists. Please Log in.",
            }
            return make_response(jsonify(responseObject), 401)
        # except Exception as ex:
        #     responseObject = {
        #         "status": "fail",
        #         "message": "Some error occured. Please try again.",
        #     }
        #     return make_response(jsonify(responseObject), 202)
