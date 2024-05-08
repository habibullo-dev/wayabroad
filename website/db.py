from pymongo import MongoClient
from .config import Config

client = MongoClient(Config.MONGODB_CONNECTION)
db = client['userDB'] 
collection = db['users'] 
