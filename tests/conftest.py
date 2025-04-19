import http.client

import pytest

from src.apps import app as application
from src.db import db


@pytest.fixture(scope="module")
def app():
    application.config.from_pyfile("test.py")
    # db.init_app(application)
    with application.app_context():
        db.create_all()
    yield application

    with application.app_context():
        db.drop_all()
