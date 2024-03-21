from flask import Flask, request, jsonify
import hashlib
import datetime
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask import Blueprint
from logging.config import dictConfig
from flask_cors import CORS
from bson import ObjectId
from dbconn import db
homePage_api = Blueprint('homePage_api', __name__)

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

homePage = Flask(__name__)
CORS(homePage)

sliders_collection = db["sliders"]
cards_collection = db["cards"]

@homePage_api.route("/addslider", methods=["POST"])
@jwt_required()
def register():
	new_slider = request.get_json() 
	doc = sliders_collection.find_one({"imgUrl": new_slider["imgUrl"]}) # check if user exist
	if not doc:
		sliders_collection.insert_one(new_slider)
		return jsonify({'msg': 'User created successfully'}), 201
	else:
		return jsonify({'msg': 'Username already exists'}), 409
     
@homePage_api.route("/sliderList", methods=["GET"])

def getList():
     try:
        data = list(sliders_collection.find())  
        
        for item in data:
            item['_id'] = str(item['_id'])
        
        return jsonify(data), 200
     except Exception as e:
        print("An error occurred:", str(e)) 
       
@homePage_api.route('/update/<string:item_id>', methods=['PUT'])
@jwt_required()
def edit_item(item_id):
    try:
        updated_data = request.json
        updated_data.pop('_id', None)
        result = sliders_collection.update_one({'_id': ObjectId(item_id)}, {'$set': updated_data})
        if result.modified_count == 1:
            return jsonify({'message': 'Item updated successfully'}),200
        else:
            return jsonify({'message': 'Item not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
@homePage_api.route("/delete/<string:item_id>", methods=["DELETE"])
@jwt_required()
def delete(item_id):
    try:
        result = sliders_collection.delete_one({'_id': ObjectId(item_id)})
        if result.deleted_count == 1:
            return jsonify({'message': 'Item deleted successfully'}),200
        else:
            return jsonify({'message': 'Item not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@homePage_api.route("/cardList", methods=["GET"])
def getCardList():
     try:
        data = list(cards_collection.find())  
        
        for item in data:
            item['_id'] = str(item['_id'])
        
        return jsonify(data), 200
     except Exception as e:
        print("An error occurred:", str(e)) 
       
@homePage_api.route('/updatecard/<string:item_id>', methods=['PUT'])
@jwt_required()
def editCard(item_id):
    try:
        updated_data = request.json
        updated_data.pop('_id', None)
        result = cards_collection.update_one({'_id': ObjectId(item_id)}, {'$set': updated_data})
        if result.modified_count == 1:
            return jsonify({'message': 'Item updated successfully'}),200
        else:
            return jsonify({'message': 'Item not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
