__author__ = 'eeamesX'
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager



app = Flask(__name__, static_url_path='', static_folder="static")
app.config.from_object('config')




db = SQLAlchemy(app)


login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = 'login'
from models import User

login_manager.login_view = "users.login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()


from .main import main as main_blueprint
app.register_blueprint(main_blueprint, url_prefix='/main')

from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint, url_prefix='/auth')

from .search import search as search_blueprint
app.register_blueprint(search_blueprint, url_prefix='/search')

from .txtadd import spider as spider_blueprint
app.register_blueprint(spider_blueprint, url_prefix='/txtadd')

from .main import views
from .auth import views

from .search import views

from app import models