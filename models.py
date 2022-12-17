from config import SQLALCHEMY_DATABASE_URI
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from cloudinary_util import cloudinaryUtils
import json
import logging
import re


cloud = cloudinaryUtils()
db = SQLAlchemy()


def setup_db(app, database_path=SQLALCHEMY_DATABASE_URI):
    logging.debug("Configuring database")
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.app_context().push()
    db.app = app
    db.init_app(app)
    db.create_all()
    logging.debug("Done configuring database")


class UserDetails(db.Model):
    """Contains the details of the user"""
    username = db.Column(db.String(), primary_key=True, nullable=False)
    password = db.Column(db.String(), nullable=False)

    def get_user_name(self) -> str:
        """returns the name of the user"""
        return self.username

    def get_user_password(self) -> str:
        """returns the password of the user"""
        return self.password

    def verify_user(self, password: str) -> bool:
        """Verifies if the given password is same as the user's password."""
        return self.password == password


class FilesData(db.Model):

    url = db.Column(db.String(), primary_key=True, nullable=False)
    label = db.Column(db.String(), nullable=False)

    def __init__(self, url: str, label: str) -> None:
        logging.debug("inserting fields to their respective attributes...")
        self.set_url(url)
        self.set_label(label)
        logging.debug("done.")

    def set_label(self, label: str) -> None:
        """Sets the label of the class"""
        #
        # validater the label
        #
        logging.debug("verifying label...")
        if (self.validate_label(label) == False):
            raise AttributeError("Invalid label")
        logging.debug("done.")
        logging.debug("setting label to {}".format(label))
        self.label = label

    def validate_label(self, label: str) -> bool:
        """Verifies that the label is a string"""
        return type(label) == str

    def set_url(self, url: str) -> None:
        """Sets the url of the file entry"""
        #
        # verify the url
        #
        logging.debug("verifying url...")
        if (self.validate_url(url) == False):
            raise AttributeError("Invalid url")
        logging.debug("done.")
        #
        # add it
        #
        logging.debug("setting url to {}".format(url))
        self.url = url

    def validate_url(self, url: str) -> bool:
        """Checks if the given string is a valid url"""

        # url length must not be greater than 256
        if len(url) > 256:
            return False

        # regex checks if the url is valid
        regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
        urls = re.findall(regex, url)
        return len(urls) == 1

    @classmethod
    def create_new_entry(cls, url: str, label: str):
        """This function creates a new entry from url and label"""
        #
        # check if file exists
        #
        logging.debug("checking if file exists in database...")
        entry_exists = FilesData.query.filter(
            FilesData.url == url).one_or_none()

        if entry_exists:
            logging.debug("file exists in database")
            raise AttributeError("File already exists in database")

        logging.debug("done: file does not exist in database.")

        #
        # create and return the class object
        #
        logging.debug("creating object...")
        return cls(url, label)

    def insert(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def format(self):
        return {
            "url": self.url,
            "label": self.label
        }

    def __repr__(self):
        return json.dumps(self.format())
