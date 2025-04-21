from flask import Flask
from flask_migrate import Migrate
from flask_restx import Api

from src.apps.user.parsers import api_namespace
from src.utils import BASE_DIR

app = Flask(
    __name__,
    # set base template
    instance_path=str(BASE_DIR / "src" / "settings"),
    instance_relative_config=True,
)

app.config.from_object(__name__)
app.config.from_pyfile("dev.py")

from src.db import db

# db.init_app(app)

migrate = Migrate(app, db)
api = Api(
    app,
    version="0.1",
    title="Doc Saving User Backend API",
    description="Save and manage documents",
    prefix="/api/users/",
)
# ? import views before adding namespace so that endpoints appears in swagger
from src.apps.user.views import PinPong

api.add_namespace(api_namespace)

from src.apps.user.models import User
