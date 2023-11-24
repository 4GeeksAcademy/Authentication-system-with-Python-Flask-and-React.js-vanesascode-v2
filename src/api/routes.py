"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_cors import CORS

api = Blueprint('api', __name__)

# Allow CORS requests to this API
CORS(api)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello teacher! In spite of all the bugs that these 4geeks templates have, (the famous 'Vanesa's error, even though it's not Vanesa's, or the misterious CORS problems after updating my old project as you explained me to do) I have been able to pass it all to another repository and make at least the registration and login work. Thank you for approving this project! (By the way, this message is comming from the backend! ;) "
    }

    return jsonify(response_body), 200
