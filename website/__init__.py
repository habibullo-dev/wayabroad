from flask import Flask
from flask_login import LoginManager
from .db import collection
import os
from dotenv import load_dotenv, find_dotenv
from flask_mail import Mail

load_dotenv(find_dotenv())

# Initialize mail here
mail = None

def create_app():
    global mail

    app = Flask(__name__)
    app.config['SECRET_KEY'] = "greenapple"
    app.config['SECURITY_PASSWORD_SALT'] = "redapple"
    
    app.config['MAIL_SERVER']='smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USERNAME'] = 'habibullochutboev@gmail.com'
    app.config['MAIL_PASSWORD'] = 'qgls phyq fchv orvs'
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False

    mail = Mail(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
   

    from .views import views
    from .auth import auth
    @login_manager.user_loader
    def load_user(user_id):
        user_data = collection.find_one({"_id": user_id})
        if user_data:
            from .auth import User
            return User(user_data) # grabbing user data from database
        return None
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(views, url_prefix='/')

    return app