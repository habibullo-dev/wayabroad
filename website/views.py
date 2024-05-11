from bson.json_util import dumps
from flask import Flask, Blueprint, render_template, jsonify
from pymongo import MongoClient
import os
from flask import request
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

PASSWORD = os.environ.get("MONGODB_PWD")
connection = f"mongodb+srv://toby:{PASSWORD}@wayabroad.ytg2mkg.mongodb.net/?retryWrites=true&w=majority&viewsName=wayabroad"

client = MongoClient(connection)
universitiesDB = client['universityDB']
blogsDB = client['blogsDB']

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('index.html')

@views.route('/blog')
def blog():
    return render_template('blog.html')

@views.route('/blog/data')
def blog_data():
    blogDB = blogsDB.blogs.find()
    data = [doc for doc in blogDB]
    return dumps(data)

@views.route('/university')
def university():
    return render_template('university.html')

@views.route('/university/data')
def university_data():
    universityDB = universitiesDB.universities.find()  # replace 'universities' with your collection name
    data = [doc for doc in universityDB]
    return dumps(data)  # convert data to JSON string

@views.route('/contact')
def contact():
    return render_template('contact.html')

@views.route('/more-info')
def more_info():
    university_name = request.args.get('university')
    university_data = universitiesDB.universities.find_one({"university_name": university_name})
    return render_template('more-info.html', data=university_data)