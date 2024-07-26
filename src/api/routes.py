"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, current_app, request, jsonify, url_for, Blueprint
from flask_jwt_extended import JWTManager, create_access_token
from models import db, User
""" from api.utils import generate_sitemap, APIException"""
from flask_cors import CORS

api = Flask(__name__)

# Allow CORS requests to this API
CORS(api)

jwt = JWTManager(api)
api.config["JWT_SECRET_KEY"] = "super-duper-secret"


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

if __name__ == '__main__':
    PORT = 3001
    api.run(host='0.0.0.0', port=PORT, debug=False)