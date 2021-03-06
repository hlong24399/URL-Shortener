import os

class Config(object):
    SECRET_KEY = os.environ.get("FLASK_SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    GOOGLE_CLIENT_ID= os.environ.get("GOOGLE_CLIENT_ID")
    GOOGLE_CLIENT_SECRET= os.environ.get("GOOGLE_CLIENT_SECRET")
