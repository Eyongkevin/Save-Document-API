import os

from src.settings.base import *

DEBUG = os.getenv("DEBUG")
TESTING = False
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")
