import hashlib
import datetime
from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from pymongo import MongoClient
from openAi import openai_api
from auth import auth_api
from flask_cors import CORS
import certifi
import os
import pymongo


app = Flask(__name__)
app.register_blueprint(openai_api, url_prefix='/openai/')
app.register_blueprint(auth_api, url_prefix='/auth/')
CORS(app)

jwt = JWTManager(app)
SECRET_KEY = os.environ.get('SECRET_KEY') or 'this is a secret'
app.config['JWT_SECRET_KEY'] = SECRET_KEY
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=1)


if __name__ == '__main__':
	app.run(debug=True)