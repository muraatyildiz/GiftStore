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
    userContent = user_request['key_words'] + "is my product to sell on my gift website application."\
    "I want to write a product description for that.Can you write a descrition whick 50 words and help seo."\
    +"And send just the description as a answer because i am passting your answer directly to website"
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
    {"role": "system", "content": "You are a helpful assistant"},
    {"role": "user", "content": userContent}
      ]
    )

    return jsonify({'msg': completion.choices[0].message.content.strip()}), 201



@openai_api.route("/alttext", methods=['GET','POST'])
def createAltText():
    user_request = request.get_json()
    userContent = user_request['key_words'] + "is my product to sell on my gift website application."\
    "I need a alt text for my product image. Can you give a meaningfull 15 words alt text which helps seo ?"\
    +"And send just the description as a answer because i am passting your answer directly to website"
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
    {"role": "system", "content": "You are a helpful assistant"},
    {"role": "user", "content": userContent}
      ]
    )
    
    return jsonify({'msg': completion.choices[0].message.content.strip()}), 201

@openai_api.route("/alttextslider", methods=['GET','POST'])
def createAltTextSlider():
    userContent = "I have a website to sell gift products."\
    "I need a alt text for my main slider images. Can you give a meaningfull 15 words alt text which helps seo ?"\
    +"And send just the description as a answer because i am passting your answer directly to website"
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
    {"role": "system", "content": "You are a helpful assistant"},
    {"role": "user", "content": userContent}
      ]
    )
    
    return jsonify({'msg': completion.choices[0].message.content.strip()}), 201

