from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('index.html')

@views.route('/blog')
def blog():
    return render_template('blog.html')

@views.route('/university')
def university():
    return render_template('university.html')

@views.route('/contact')
def contact():
    return render_template('contact.html')
