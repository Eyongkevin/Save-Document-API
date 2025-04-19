from flask_restx import fields

from src.apps import api

register_serializer = api.model(
    "RegisterLobin",
    {"username": fields.String, "email": fields.String, "password": fields.String},
)
