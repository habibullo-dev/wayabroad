import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class Config:
    MONGODB_PWD = os.environ.get("MONGODB_PWD")
    MONGODB_CONNECTION = f"mongodb+srv://toby:{MONGODB_PWD}@wayabroad.ytg2mkg.mongodb.net/?retryWrites=true&w=majority&appName=wayabroad"
