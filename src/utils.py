import base64
import hashlib
import os
from pathlib import Path

import bcrypt

BASE_DIR = Path(__file__).resolve().parent.parent


def generate_password_hash(password: str):
    BCRYPT_SALT = os.getenv("BCRYPT_SALT")
    return bcrypt.hashpw(
        encode_password(password),
        BCRYPT_SALT.encode("UTF8"),
    ).decode()


def encode_password(password: str) -> bytes:
    """Maximum Password Length

    The bcrypt algorithm only handles passwords up to 72 characters,
    any characters beyond that are ignored. To work around this,
    a common approach is to hash a password with a cryptographic hash (such as sha256)
    and then base64 encode it to prevent NULL byte problems before hashing the result with bcrypt:

    source: https://pypi.org/project/bcrypt/
    """

    return base64.b64encode(hashlib.sha256(password.encode("UTF8")).digest())
