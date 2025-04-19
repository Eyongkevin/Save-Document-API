import base64
import hashlib
import os
from pathlib import Path

import bcrypt

BASE_DIR = Path(__file__).resolve().parent.parent


def generate_password_hash(password: str):
    BCRYPT_SALT = os.getenv("BCRYPT_SALT")
    return bcrypt.hashpw(
        base64.b64encode(hashlib.sha256(password.encode("UTF8")).digest()),
        BCRYPT_SALT.encode("UTF8"),
    ).decode()
