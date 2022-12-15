import cloudinary.api
import cloudinary.uploader
import json
import os

import cloudinary

cloudinaryConfig = cloudinary.config(
    cloud_name=os.environ.get("CLOUDNAME"),
    api_key=os.environ.get("CLOUDAPIKEY"),
    api_secret=os.environ.get("CLOUDINARYSECRET"),
    secure=True
)


class cloudinaryUtils():
    def uploadFile(self, file):
        cloudinary_response = cloudinary.uploader.upload(file)
        print("Cloudinary response: ", json.dumps(cloudinary_response))
        return cloudinary_response
