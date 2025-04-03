import os

from src.settings.base import *

DEBUG = os.getenv("DEBUG")
TESTING = os.getenv("TESTING")
