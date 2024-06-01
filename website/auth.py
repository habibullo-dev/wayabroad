import os
import re
from pymongo import MongoClient
from flask_login import LoginManager, UserMixin, login_user, logout_user
from flask_mail import Mail, Message
from dotenv import load_dotenv, find_dotenv
from itsdangerous import URLSafeTimedSerializer
from email_validator import validate_email, EmailNotValidError
from werkzeug.security import check_password_hash, generate_password_hash
from flask import Blueprint, url_for, redirect, flash, request, render_template, session, current_app
from . import mail
from flask import current_app as app

load_dotenv(find_dotenv())

PASSWORD = os.environ.get("MONGODB_PWD")

auth = Blueprint('auth', __name__)

password = os.environ.get("MONGODB_PWD")
connection = f"mongodb+srv://toby:{PASSWORD}@wayabroad.ytg2mkg.mongodb.net/?retryWrites=true&w=majority&appName=wayabroad"

client = MongoClient(connection)
db = client['userDB'] 
collection = db['users'] 

class User(UserMixin):
    def __init__(self, data):
        self.id = data["_id"]
        self.password = data["password"]

    @staticmethod
    def get(user_id):
        data = collection.find_one({"_id": user_id})
        if data:
            return User(data)
        return None

    def get_reset_token(self, expires_sec=1800):
        s = URLSafeTimedSerializer(app.config['SECRET_KEY'])
        return s.dumps(self.id, salt='sweetbananas')  # Change this line

    @staticmethod
    def verify_reset_token(token):
        s = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token, salt='sweetbananas', max_age=1800)  # Change this line
        except SignatureExpired:
            return None  # valid token, but expired
        except BadTimeSignature:
            return None  # invalid token
        user = User.get(user_id)
        return user

@auth.route('/register', methods=['GET'])
def register():
    return render_template('register.html')

@auth.route('/register', methods=['POST'])
def signup():
    # Get the user's information from the request
    fullname = request.form.get('fullname')
    email = request.form.get('email')
    password = request.form.get('password')
    find_us_options = request.form.get('findUsOptions')

    # Validate email
    try:
        v = validate_email(email)  # validate and get info
        email = v["email"]  # replace with normalized form
    except EmailNotValidError as e:
        # email is not valid, handle exception
        flash('Please provide a valid email address.', 'danger')
        return redirect(url_for('auth.register'))

    # Validate password
    password_regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$"
    if not re.match(password_regex, password):
        flash('Password must contain at least one uppercase letter, one lowercase letter, one number, and be at least 8 characters long.', 'warning')
        return redirect(url_for('auth.register'))

    # Check if a user with the given email already exists
    user = collection.find_one({"email": email})

    if user:  # if a user is found, we want to redirect back to signup page so user can try again
        flash('Email address already exists', 'danger')
        return redirect(url_for('auth.register'))

    # Hash the password before storing it
    password_hash = generate_password_hash(password, method='pbkdf2:sha256')

    # Store the data in MongoDB
    user_data = {
        "_id": email, 
        "fullname": fullname,
        "email": email,
        "password": password_hash,
        "find_us_options": find_us_options,
    }
    collection.insert_one(user_data)

    session['user'] = email  # set the session variable

    user = User(user_data)  # create a User object
    login_user(user)  # log in the user

    flash(f'Welcome to our website {fullname}!', 'success')
    return render_template('register.html', user_created=True)

@auth.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def signin():
    email = request.form.get('email')
    password = request.form.get('password')

    # Validate email
    try:
        v = validate_email(email)  # validate and get info
        email = v["email"]  # replace with normalized form
    except EmailNotValidError as e:
        # email is not valid, handle exception
        flash('Please provide a valid email address.', 'danger')
        return redirect(url_for('auth.login'))

    # Validate password
    if not password:
        flash('Please provide a password.', 'danger')
        return redirect(url_for('auth.login'))

    # Check if the user exists in the database
    user = User.get(email)
    if user and check_password_hash(user.password, password):
        login_user(user)  # log in the user
        flash('Successfully logged in!', 'success')
        return render_template("login.html", user_created=True)

    flash('Please check your login details and try again.', 'danger')
    return redirect(url_for('auth.login'))  # if user doesn't exist or password is wrong, reload the page

@auth.route('/logout')
def logout():
    logout_user()
    #flash('You have been logged out.', 'success')
    return redirect(url_for('views.home'))

@auth.route('/forgot-password')
def forgot_password():
    return render_template('forgot-password.html')

@auth.route('/reset-password/', methods=['GET', 'POST'])
def reset_password():
    return render_template('reset-password.html')

@auth.route('/forgot-password', methods=['POST'])
def send_reset_email():
    email = request.form.get('email')

    # Validate email
    try:
        v = validate_email(email)  # validate and get info
        email = v["email"]  # replace with normalized form
    except EmailNotValidError as e:
        # email is not valid, handle exception
        flash('Please provide a valid email address.', 'danger')
        return redirect(url_for('auth.forgot_password'))

    # Check if the user exists in the database
    user = User.get(email)
    if user:
        # Generate a reset token
        token = user.get_reset_token()

        # Generate the reset password link with the token as a query parameter
        reset_link = url_for('auth.reset_password_token', token=token, _external=True)

        # Send an email to the user with the reset link
        msg = Message('Password Reset Request',
                      sender='noreply@demo.com',
                      recipients=[user.id])
        msg.body = f'''To reset your password, visit the following link:
{reset_link}

If you did not make this request then simply ignore this email and no changes will be made.
'''
        mail.send(msg)

        flash('An email has been sent with instructions to reset your password.', 'info')
    else:
        flash('No account found with that email.', 'warning')

    return redirect(url_for('auth.forgot_password'))

@auth.route('/new-password/', methods=['GET', 'POST'])
def reset_password_token():
    token = request.args.get('token')
    if not token:
        flash('Invalid token', 'danger')
        return redirect(url_for('auth.forgot_password'))

    user = User.verify_reset_token(token)
    if not user:
        flash('That is an invalid or expired token', 'warning')
        return redirect(url_for('auth.forgot_password'))

    if request.method == 'POST':
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        if password != confirm_password:
            flash('Passwords do not match.', 'warning')
            return redirect(url_for('auth.reset_password'))

        password_regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$"
        if not re.match(password_regex, password):
            flash('Password must contain at least one uppercase letter, one lowercase letter, one number, and be at least 8 characters long.', 'warning')
            return redirect(url_for('auth.reset_password'))

        password_hash = generate_password_hash(password, method='pbkdf2:sha256')
        collection.update_one({"_id": user.id}, {"$set": {"password": password_hash}})
        logout_user()
        flash('Your password has been updated! Please login again', 'success')
        return redirect(url_for('auth.login'))

    return render_template('reset-password.html', token=token)

