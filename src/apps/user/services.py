from sqlalchemy.exc import IntegrityError

from src.apps import db
from src.apps.user.models import User


def register(username, email, password):
    try:
        user = User(username, email, password)
        db.session.add(user)
        db.session.commit()
        return user
    except IntegrityError as ex:
        raise PermissionError("User already exists. Please Login.") from ex
