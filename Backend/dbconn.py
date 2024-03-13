from pymongo import MongoClient
import os
import certifi

DATABASE_LINK= os.environ.get('DATABASE_LINK') 

client = MongoClient(DATABASE_LINK,tlsCAFile=certifi.where())
db = client["web"]