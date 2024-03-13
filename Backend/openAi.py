from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from openai import OpenAI
from dotenv import load_dotenv
from flask import Blueprint
from logging.config import dictConfig
from flask_cors import CORS

openai_api = Blueprint('openai_api', __name__)

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

openai = Flask(__name__)
CORS(openai)
load_dotenv()
client = OpenAI()

@openai_api.route("/description", methods=['GET','POST'])
@jwt_required()
def createDescription():
    user_request = request.get_json()
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
    {"role": "system", "content": "You are a helpful assistant"},
    {"role": "user", "content": user_request['key_words']}
      ]
    )

    # print(completion)
    # mesajdaki semboller silenecek 
    # aciklama icin en iyi mesajlar buluanacak
    # diger metodlar yapialcak
    return jsonify({'msg': completion.choices[0].message.content.strip()}), 201

@openai_api.route("/filename", methods=['GET','POST'])
def createFilename():
    print('test')
    return jsonify({'msg': 'filename created successfully'}), 201

@openai_api.route("/alttext", methods=['GET','POST'])
def createAltText():
    print('test')
    return jsonify({'msg': 'alttext created successfully'}), 201

