from flask import Flask, request, jsonify
import hashlib
import datetime
from pymongo import MongoClient
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask import Blueprint
from logging.config import dictConfig
from flask_cors import CORS
import pymongo
import certifi
auth_api = Blueprint('auth_api', __name__)

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

auth = Flask(__name__)
CORS(auth)


client = MongoClient("mongodb+srv://mrtyldz2350:XZbPxZdz4B9FqMj4@cluster2.tczpjji.mongodb.net/?retryWrites=true&w=majority&appName=Cluster2",tlsCAFile=certifi.where())
db = client["web"]
users_collection = db["users"]

@auth_api.route("/add", methods=["POST"])
@jwt_required()
def register():
	new_user = request.get_json() # store the json body request
	new_user["password"] = hashlib.sha256(new_user["password"].encode("utf-8")).hexdigest() # encrpt password
	doc = users_collection.find_one({"username": new_user["username"]}) # check if user exist
	if not doc:
		users_collection.insert_one(new_user)
		return jsonify({'msg': 'User created successfully'}), 201
	else:
		return jsonify({'msg': 'Username already exists'}), 409

@auth_api.route("/login", methods=["POST"])
def login():
	login_details = request.get_json()
	user_from_db = users_collection.find_one({'username': login_details['username']}) 

	if user_from_db:
		encrpted_password = hashlib.sha256(login_details['password'].encode("utf-8")).hexdigest()
		if encrpted_password == user_from_db['password']:
			access_token = create_access_token(identity=user_from_db['username']) 
		return jsonify(access_token=access_token,username= user_from_db['username'],role= user_from_db['role']), 200

	return jsonify({'msg': 'The username or password is incorrect'}), 401

@auth_api.route("/userInfo", methods=["GET"])
@jwt_required()
def profile():
	current_user = get_jwt_identity() 
	user_from_db = users_collection.find_one({'username' : current_user})
	if user_from_db:
		del user_from_db['_id'], user_from_db['password'] 
		return jsonify({'profile' : user_from_db }), 200
	else:
		return jsonify({'msg': 'Profile not found'}), 404
