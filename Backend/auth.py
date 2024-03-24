from flask import Flask, request, jsonify
import hashlib
import datetime
from flask_jwt_extended import JWTManager,create_refresh_token, create_access_token, jwt_required, get_jwt_identity,get_jwt_identity, jwt_required, get_jwt
from flask import Blueprint
from logging.config import dictConfig
from flask_cors import CORS
from bson import ObjectId
from dbconn import db
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

users_collection = db["users"]
blacklist_collection = db["blacklist"]
jwt = JWTManager(auth)

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
            refresh_token = create_refresh_token(identity=user_from_db['username'])
            return jsonify(access_token=access_token, refresh_token=refresh_token, username=user_from_db['username'], role=user_from_db['role']), 200

    return jsonify({'msg': 'The username or password is incorrect'}), 401

@auth_api.route("/logout", methods=["DELETE"])
@jwt_required()
def logout():
    try:
        jti = get_jwt()['jti'] 
        blacklist_collection.insert_one({'jti': jti})  
        return jsonify({'message': 'Successfully logged out'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@jwt.token_in_blocklist_loader
def check_if_token_in_blocklist(decrypted_token):
    jti = decrypted_token['jti']
    return bool(blacklist_collection.find_one({'jti': jti}))

    
@auth_api.route("/userInfo", methods=["GET"])
@jwt_required()
def profile():
	current_user = get_jwt_identity() 
	user_from_db = users_collection.find_one({'username' : current_user})
	if user_from_db:
		del user_from_db['_id'], user_from_db['password'] 
		return jsonify({'user' : user_from_db }), 200
	else:
		return jsonify({'msg': 'Profile not found'}), 404
	
@auth_api.route("/userList", methods=["GET"])
@jwt_required()
def getList():
    data = list(users_collection.find({},{"password": 0}))  # Retrieve all documents from the collection
    
    # Convert ObjectId to string representation
    for item in data:
        item['_id'] = str(item['_id'])

    return jsonify(data),200

@auth_api.route('/update/<string:item_id>', methods=['PUT'])
@jwt_required()
def edit_item(item_id):
    try:
        updated_data = request.json
        updated_data.pop('_id', None)
        updated_data.pop('password', None)
        result = users_collection.update_one({'_id': ObjectId(item_id)}, {'$set': updated_data})
        if result.modified_count == 1:
            return jsonify({'message': 'Item updated successfully'}),200
        else:
            return jsonify({'message': 'Item not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
@auth_api.route("/delete/<string:item_id>", methods=["DELETE"])
@jwt_required()
def delete(item_id):
    try:
        result = users_collection.delete_one({'_id': ObjectId(item_id)})
        if result.deleted_count == 1:
            return jsonify({'message': 'Item deleted successfully'}),200
        else:
            return jsonify({'message': 'Item not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
