import os
from urllib.parse import quote_plus
from settings import DB_HOST, DB_NAME, DB_PASSWORD, DB_USER


SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))


DB_PATH = 'postgresql+psycopg2://{}:{}@{}/{}'.format(
    DB_USER, DB_PASSWORD, DB_HOST, DB_NAME)

DEBUG = True

SQLALCHEMY_DATABASE_URI = DB_PATH
