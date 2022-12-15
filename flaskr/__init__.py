from flask import Flask, request, abort, jsonify
from models import setup_db, db, FilesData, UserDetails
from flask_cors import CORS
from models import FilesData
import sys
from flask_moment import Moment
from flask_migrate import Migrate
import json

# to be removed
import time


def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app, resources={
         r"/api/": {"origins": "http://localhost:3000"}})
    moment = Moment(app)
    migrate = Migrate(app, db)

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

    @app.route("/upload", methods=["POST"])
    def upload_photo():
        try:
            print("Received request to add new file data")
            file = request.files.get("file")

            print("Request file: ", file)

            print("creating new FilesData model...")
            file_data = FilesData.create_new_file(file)
            print("done.")

            # Insert file data into database
            print("Inserting data into database...")
            new_file_data = file_data.insert()
            print("done inserting data into database")

            # return success and new file data
            return_data = {
                "success": True,
                "fileData": new_file_data
            }
            print("Returning: ", json.dumps(return_data))
            return jsonify({"success": True, "fileData": return_data})
        except:
            print(sys.exc_info())
            abort(400)

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
