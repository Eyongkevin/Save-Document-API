from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from src.apps.user.views import user
from src.utils import BASE_DIR

app = Flask(
    __name__,
    # set base template
    instance_path=str(BASE_DIR / "src" / "settings"),
    instance_relative_config=True,
)

app.config.from_object(__name__)
app.config.from_pyfile("dev.py")

db = SQLAlchemy(app)

app.register_blueprint(user)
from src.apps.user import models

with app.app_context():
    db.create_all()
