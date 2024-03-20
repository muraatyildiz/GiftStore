import json
from flask import Flask, request, jsonify
import hashlib
import datetime
from math import ceil
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask import Blueprint
from logging.config import dictConfig
from flask_cors import CORS
from bson import ObjectId
from dbconn import db
import re
from flask import Blueprint

product_api = Blueprint('product_api', __name__)

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
product = Flask(__name__)
CORS(product)

users_collection = db["users"]
products_collection = db["products"]

@product_api.route("/add", methods=['POST'])
@jwt_required()
def add():
   new_product = request.get_json()
   doc = products_collection.find_one({"name": new_product["name"]}) # check if user exist
   products_collection.create_index([("name", "text"), ("description", "text"), ("category", "text")])
   if not doc:
        products_collection.insert_one(new_product)
        return jsonify({'msg': 'Product created successfully'}), 201
   else:
      return jsonify({'msg': 'Product already exists'}), 409

@product_api.route('/update/<string:item_id>', methods=['PUT']) 
def update(item_id):
    try:
        updated_data = request.json
        updated_data.pop('_id', None)
        result = products_collection.update_one({'_id': ObjectId(item_id)}, {'$set': updated_data})
        if result.modified_count == 1:
            return jsonify({'message': 'Item updated successfully'}),200
        else:
            return jsonify({'message': 'Item not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@product_api.route("/list", methods=['GET'])
def sendList(): 
    page = int(request.args.get('page', 1))  
    page_size = int(request.args.get('page_size', 12))  
    search_term = request.args.get('search', '')  
    category = request.args.get('category', '') 
    min_price = float(request.args.get('minPrice', 0))  
    max_price = float(request.args.get('maxPrice', float('inf')))
    query = {}  

    if search_term:
        regex_pattern = re.compile(search_term, re.IGNORECASE)
        query = {
            "$or": [
                {"name": {"$regex": regex_pattern}},
                {"description": {"$regex": regex_pattern}},
                {"category": {"$regex": regex_pattern}}
            ]
        }
    if category: 
        query["category"] = category
    query["price"] = {"$gte": min_price, "$lte": max_price}
    print('sddsdsdsdsd',query)
    total_documents = products_collection.count_documents(query) 
    total_pages = ceil(total_documents / page_size)
    skip = (page - 1) * page_size
    data = list(products_collection.find(query).skip(skip).limit(page_size))

    min_price_doc = products_collection.find_one({}, sort=[("price", 1)])
    min_price = float(min_price_doc["price"]) if min_price_doc else 0

    max_price_doc = products_collection.find_one({}, sort=[("price", -1)])
    max_price = float(max_price_doc["price"]) if max_price_doc else float('inf')
    for item in data:
        item['_id'] = str(item['_id'])

    return jsonify({'products': data, 'total':total_documents, 'total_pages': total_pages, 'min_price':min_price,'max_price':max_price}), 200

@product_api.route("/admin/list", methods=['GET'])
@jwt_required()
def sendAdminList(): 
    data = list(products_collection.find({})) 
    for item in data:
        item['_id'] = str(item['_id'])

    return jsonify({'products': data}), 200
@product_api.route("/getByCategory/<string:category>", methods=['GET', 'POST'])
def getListCategory(category):
  return "getbyCatehory" 
@product_api.route("/getBySearch/<string:search>", methods=['GET', 'POST'])
def getListSearch(search):
  return "search"


@product_api.route("/delete/<string:item_id>", methods=["DELETE"])
@jwt_required()
def delete_items(item_id):
    try:
        result = products_collection.delete_one({'_id': ObjectId(item_id)})
        if result.deleted_count == 1:
            return jsonify({'message': 'Item deleted successfully'}),200
        else:
            return jsonify({'message': 'Item not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
