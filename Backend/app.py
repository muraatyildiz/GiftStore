import hashlib
import datetime
from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from pymongo import MongoClient
from openAi import openai_api
from auth import auth_api
from product import product_api
from fileUpload import fileUpload_api
from flask_cors import CORS
import certifi
import os
import pymongo


app = Flask(__name__)
app.register_blueprint(openai_api, url_prefix='/openai/')
app.register_blueprint(auth_api, url_prefix='/auth/')
app.register_blueprint(product_api, url_prefix='/product/')
app.register_blueprint(fileUpload_api, url_prefix='/file/')
CORS(app)

jwt = JWTManager(app)
SECRET_KEY = os.environ.get('SECRET_KEY') or 'this is a secret'
app.config['JWT_SECRET_KEY'] = SECRET_KEY
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=1)

 
if __name__ == '__main__':
	# app.run(debug=True)
	app.run(host='0.0.0.0',port='8080')