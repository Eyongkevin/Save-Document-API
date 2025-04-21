import http.client

import bcrypt
from flask import jsonify, make_response, request
from flask_restx import Resource

from src.apps import app
from src.apps.user import services, token_authentication
from src.apps.user.parsers import api_namespace, registration_parser
from src.apps.user.serializers import login_request_serializer, register_serializer
from src.utils import encode_password


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
            return make_response(jsonify(responseObject), http.client.CREATED)
        except PermissionError:
            responseObject = {
                "status": "fail",
                "message": "User already exists. Please Log in.",
            }
            return make_response(jsonify(responseObject), http.client.UNAUTHORIZED)
        except Exception as ex:
            responseObject = {
                "status": "fail",
                "message": f"Some error occured: {ex}. Please try again.",
            }
            return make_response(jsonify(responseObject), http.client.ACCEPTED)


@api_namespace.route("/auth/login/")
class Login(Resource):
    @api_namespace.doc("auth_login")
    @api_namespace.expect(login_request_serializer)
    def post(self):
        """Login User"""

        username = api_namespace.payload["username"]
        password = api_namespace.payload["password"]

        try:
            user = services.fetch_user_by_username(username)
            if user and bcrypt.checkpw(
                encode_password(password), user.password.encode("utf8")
            ):
                auth_token = token_authentication.generate_token_header(
                    username, app.config["PRIVATE_KEY"]
                )
                if auth_token:
                    resObj = {
                        "status": "success",
                        "message": "Successfully logged in",
                        "auth_token": auth_token,
                    }
                    return make_response(jsonify(resObj), http.client.OK)
                resObj = {"status": "fail", "message": "token generation failed"}
                return make_response(jsonify(resObj), http.client.ACCEPTED)
            else:
                resObj = {
                    "status": "fail",
                    "message": "username or password incorrect. Try again",
                }
                return make_response(jsonify(resObj), http.client.UNAUTHORIZED)
        except Exception:
            resObj = {
                "status": "fail",
                "message": "Some error occured. Please try again.",
            }
            return make_response(jsonify(resObj), http.client.ACCEPTED)
