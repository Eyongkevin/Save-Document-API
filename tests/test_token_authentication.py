import datetime

from src.apps import app
from src.apps.user import token_authentication

from .constants import INVALID_PUBLIC_KEY

PRIVATE_KEY = app.config["PRIVATE_KEY"]
PUBLIC_KEY = app.config["PUBLIC_KEY"]


def test_encode_and_decode():
    payload = {"text": "testing example"}
    token = token_authentication.encode_token(payload, PRIVATE_KEY)
    assert payload == token_authentication.decode_token(token, PUBLIC_KEY)


def test_invalid_token_header_invalid_format():
    header = "Bea header"
    result = token_authentication.validate_token_header(header, PUBLIC_KEY)
    assert None is result  # TokenFormatError


def test_invalid_token_header_bad_token():
    header = "Bearer notvalidtoken"
    result = token_authentication.validate_token_header(header, PUBLIC_KEY)
    assert result is None  # InvalidTokenError


def test_invalid_token_no_header():
    header = None
    result = token_authentication.validate_token_header(header, PUBLIC_KEY)
    assert result is None  # NoTokenError


def test_invalid_token_header_not_expiry_time():
    payload = {"username": "tonyparker"}
    token: str = token_authentication.encode_token(payload, PRIVATE_KEY)
    header = f"Bearer {token}"
    result = token_authentication.validate_token_header(header, PUBLIC_KEY)
    assert result is None  # TokenNoExpiryDateError


def test_invalid_token_header_expired():
    expiry = datetime.datetime.now(datetime.UTC) - datetime.timedelta(days=2)
    payload = {
        "username": "tonyparker",
        "exp": expiry,
    }
    token = token_authentication.encode_token(payload, PRIVATE_KEY)
    header = f"Bearer {token}"
    result = token_authentication.validate_token_header(header, PUBLIC_KEY)
    assert result is None  # TokenExpiredError


def test_invalid_token_header_no_username():
    expiry = datetime.datetime.now(datetime.UTC) + datetime.timedelta(days=2)
    payload = {
        "exp": expiry,
    }
    token = token_authentication.encode_token(payload, PRIVATE_KEY)
    header = f"Bearer {token}"
    result = token_authentication.validate_token_header(header, PUBLIC_KEY)
    assert result is None  # TokenNoUsernameError


def test_valid_token_header_invalid_key():
    header = token_authentication.generate_token_header("tonyparker", PRIVATE_KEY)
    result = token_authentication.validate_token_header(header, INVALID_PUBLIC_KEY)
    assert result is None  # TokenInvalidPublicKeyError


def test_valid_token_header():
    username = "tonyparker"
    header = token_authentication.generate_token_header(username, PRIVATE_KEY)
    result = token_authentication.validate_token_header(header, PUBLIC_KEY)
    assert result == username
