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


def fetch_user_by_username(username: str):
    """Fetch user by username"""

    return User.query.filter_by(username=username).first()
