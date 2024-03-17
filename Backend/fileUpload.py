from flask import Flask, request, send_from_directory
from werkzeug.exceptions import RequestEntityTooLarge
from werkzeug.utils import secure_filename
from flask import Blueprint
from flask_cors import CORS
from openAi import createFilename
import os
import json

 
fileUpload_api = Blueprint('fileUpload_api', __name__)
fileUpload = Flask(__name__)
fileUpload.config['UPLOAD_DIRECTORY'] = 'uploads/'
fileUpload.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 # 16MB
fileUpload.config['ALLOWED_EXTENSIONS'] = ['.jpg', '.jpeg', '.png', '.gif']

CORS(fileUpload) 


@fileUpload_api.route('/upload', methods=['POST'])
def upload():
  try:
    file = request.files['file']
    createFilename()
    if file:
      extension = os.path.splitext(file.filename)[1].lower()

      if extension not in fileUpload.config['ALLOWED_EXTENSIONS']:
        return 'File is not an image.'
        
      file.save(os.path.join(
        fileUpload.config['UPLOAD_DIRECTORY'],
        secure_filename(file.filename)
      ))
  
  except RequestEntityTooLarge:
    return 'File is larger than the 16MB limit.'
  
  response={'Results':secure_filename(file.filename)}
  ret=fileUpload.response_class(
    response=json.dumps(response),
    status=200,
    mimetype='application/json'
  )
  return ret #Return the data in a string format

@fileUpload_api.route('/serve-image/<filename>', methods=['GET'])
def serve_image(filename):
  print( "filename",filename)
  
  return send_from_directory(fileUpload.config['UPLOAD_DIRECTORY'], filename)