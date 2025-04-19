import os

from src.settings.dev import *

DEBUG = os.getenv("DEBUG")
TESTING = os.getenv("TESTING")
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI_TEST")
