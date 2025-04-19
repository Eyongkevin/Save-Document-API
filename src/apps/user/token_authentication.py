import datetime
import logging

import jwt
from parse import parse

logger = logging.getLogger(__name__)


def encode_token(payload, private_key):
    return jwt.encode(payload, private_key, algorithm="RS256")


def decode_token(token, public_key):
    return jwt.decode(token, public_key, algorithms="RS256")


def generate_token_header(username: str, private_key: str):
    """
    Generate a token header based on the username, Sign using the private key
    """

    payload = {
        "username": username,
        "iat": datetime.datetime.now(datetime.UTC),
        "exp": datetime.datetime.now(datetime.UTC) + datetime.timedelta(days=2),
    }
    token = encode_token(payload, private_key)
    # token = token.decode("utf8")
    return f"Bearer {token}"


def validate_token_header(header, public_key):
    """
    Validate that a token header is correct

    If correct, it return the username, if not, it
    returns None
    """

    if not header:
        logger.info("No header")
        return None
    # Retrieve the Bearer token
    parse_result = parse("Bearer {}", header)
    if not parse_result:
        logger.info(f'Wrong format for header "{header}"')
        return None
    token = parse_result[0]
    try:
        decoded_token = decode_token(token, public_key)
    except jwt.exceptions.DecodeError:
        logger.warning(f'Error decoding header "{header}" with given public key')
        return None
    except jwt.exceptions.ExpiredSignatureError:
        logger.error(f"Authentication header was expired.")
        return None
    except jwt.exceptions.InvalidKeyError:
        logger.error(f"Authentication header is invalid")
        return None

    # Check expiry is in the token
    if "exp" not in decoded_token:
        logger.warning("Token does not have expiry (exp)")
        return None

    # Check username is in the token
    if "username" not in decoded_token:
        logger.warning("Token does not have username")
        return None

    logger.info("Header successfully validated")
    return decoded_token["username"]
