import http.client

import pytest
from faker import Faker

from src.apps import app as application
from src.apps.user.models import User
from src.db import db

fake = Faker()


@pytest.fixture(scope="session")
def app():
    application.config.from_pyfile("test.py")
    db.init_app(application)
    with application.app_context():
        db.create_all()
    yield application

    with application.app_context():
        db.drop_all()


@pytest.fixture
def user_fixture(app):
    """Generate three users"""

    users = []
    user_models = []
    for _ in range(3):
        user = {
            "username": fake.user_name(),
            "email": fake.email(),
            "password": fake.password(),
        }
        user_model = User(**user)
        with app.app_context():
            db.session.add(user_model)
            db.session.commit()
        users.append(user)
        user_models.append(user_model)

    yield users

    for user in user_models:
        with app.app_context():
            db.session.delete(user)
            db.session.commit()
