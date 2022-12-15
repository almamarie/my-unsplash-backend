import os

DB_HOST = os.getenv('DB_HOST', '0.0.0.0:$PORT')
DB_USER = os.getenv('DB_USER', 'marieloumar')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'postgres')
DB_NAME = os.getenv('DB_NAME', 'fileupload')
DEBUG=os.getenv('DEBUG', True)