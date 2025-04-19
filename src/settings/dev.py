import os

from src.settings.base import *

DEBUG = os.getenv("DEBUG")
TESTING = False
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")
PUBLIC_KEY = os.getenv("PUBLIC_KEY")

PRIVATE_KEY = os.getenv("PRIVATE_KEY")
