import re

import pytest


def test_db_is_for_testing(app):
    assert (
        re.search(r"test", app.config["SQLALCHEMY_DATABASE_URI"].split("/")[-1])
        is not None
    )
