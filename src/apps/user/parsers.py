from flask_restx import Namespace

api_namespace = Namespace("v1", description="Users API operations")

registration_parser = api_namespace.parser()
registration_parser.add_argument(
    "username", type=str, required=True, location="form", help="User's username"
)
registration_parser.add_argument(
    "email", type=str, required=True, location="form", help="User's email"
)
registration_parser.add_argument(
    "password", type=str, required=True, location="form", help="User's password"
)
