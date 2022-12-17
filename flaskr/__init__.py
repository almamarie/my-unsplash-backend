import time
from flask import Flask, request, abort, jsonify
from models import setup_db, db, FilesData, UserDetails
from flask_cors import CORS
from models import FilesData
import sys
from flask_moment import Moment
from flask_migrate import Migrate
import logging

# set up logging
logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {levelname:<8} {message}",
                    style="{",
                    # filename='{}logs'.format(__file__[:-2]),
                    # filemode='w'
                    )

# to be removed


def create_app(test_config=None):
    logging.debug("configuring app...")
    app = Flask(__name__)
    setup_db(app)
    CORS(app, resources={
         r"/api/": {"origins": "http://localhost:3000/*"}})
    moment = Moment(app)
    migrate = Migrate(app, db)
    logging.debug("done.")

    @app.after_request
    def after_request(response):
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type,Authorization,true"
        )

        response.headers.add(
            "Access-Control-Allow-Methods", "GET,POST,DELETE"
        )

        response.headers.add(
            'Access-Control-Allow-Origin', 'http://localhost:3000'
        )

        response.headers.add(
            'Access-Control-Allow-Credentials', 'true'
        )

        return response

    @app.route("/")
    def main_route():
        return jsonify({"success": True, "message": "Configuration Successful"})

    @app.route("/new-photo", methods=["POST"])
    def upload_photo():
        """creates a new photo entry"""

        try:
            print("request: ", request)
            body: dict = request.get_json()
            logging.debug("received request to add new file.")
            logging.debug("requedst data: {}".format(body))

            # create the new entry
            file_entry_object = FilesData.create_new_entry(
                body.get("url"), body.get("label"))

            # Add data to database
            logging.debug("adding data to database")
            file_entry_object.insert()
            return jsonify({"success": True})
        except:
            print(sys.exc_info())
            abort(400)

    @app.route("/all-file-data")
    def fetch_all_file_data() -> dict:
        # fetch all the file data from the database
        all_file_data: list = FilesData.query.all()

        # format the files data
        formated_data: list[dict] = [file_data.format()
                                     for file_data in all_file_data]

        # return the data
        return jsonify({
            "success": True,
            "items": formated_data,
            "totalNumber": len(formated_data)
        })

    @app.errorhandler(404)
    def not_found(error):
        return (
            jsonify({"success": False, "error": 404,
                    "message": "resource not found"}),
            404,
        )

    @app.errorhandler(422)
    def unprocessable(error):
        return (
            jsonify({"success": False, "error": 422,
                    "message": "unprocessable"}),
            422,
        )

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({"success": False, "error": 400, "message": "bad request"}), 400

    @app.errorhandler(405)
    def not_found(error):
        return (
            jsonify({"success": False, "error": 405,
                    "message": "method not allowed"}),
            405,
        )

    @app.errorhandler(500)
    def server_error(error):
        return (
            jsonify({"success": False, "error": 500,
                    "message": "server error"}),
            500,
        )

    return app
