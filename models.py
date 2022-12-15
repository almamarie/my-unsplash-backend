from config import SQLALCHEMY_DATABASE_URI
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from cloudinary_util import cloudinaryUtils
import json
import logging


cloud = cloudinaryUtils()
db = SQLAlchemy()


def setup_db(app, database_path=SQLALCHEMY_DATABASE_URI):
    logging.info("Configuring database")
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.app_context().push()
    db.app = app
    db.init_app(app)
    db.create_all()
    logging.info("Done configuring database")


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


class FilesData(db.Model):

    url = db.Column(db.String(), primary_key=True, nullable=False)
    label = db.Column(db.String(), nullable=False)

    def __init__(self, data):
        print("inserting fields in their respective attributes...")
        try:
            self.file_name = data.get("name")
            self.public_id = data.get("publicId")
            self.file_url = data.get("url")
            self.upload_date = data.get("uploadDate")
        except:
            raise Exception("Missing fields")
        print("done.")

    @classmethod
    def create_new_file(cls, file):
        print("checking if file exists in data...")
        file_in_database = FilesData.query.filter(
            FilesData.file_name == file.filename).one_or_none()

        if file_in_database:
            print("file exists in database")
            raise Exception("File already exists in database")

        print("done: file does not exist in database.")

        # upload file
        print("uploading file...")
        upload_data = cloud.uploadFile(file)
        print("done.")

        data = {
            "name": file.filename,
            "publicId": upload_data.get("public_id"),
            'url': upload_data.get('url'),
            "uploadDate": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        }
        print("creating object...")
        return cls(data)

    def insert(self) -> None:

        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def format(self):
        return

    def __repr__(self):
        return json.dumps(self.format())
