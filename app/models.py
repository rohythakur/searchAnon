__author__ = 'eeamesX'
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app, request, url_for
from flask_login import UserMixin, AnonymousUserMixin, current_user, logout_user, flash, login_user
from app import db, login_manager
from datetime import datetime




##Todo Upgrade Item for better links ie last checked

class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(64))
    link = db.Column(db.String(64), unique=True)
    description = db.Column(db.Text)
    member_since = db.Column(db.DateTime(), default=datetime.utcnow)
    last_updated = db.Column(db.DateTime(), default=datetime.utcnow)
    click_count = db.Column(db.Integer())


    def __init__(self, title, link, description, member_since, last_updated, click_count):
        self.title = title
        self.link = link
        self.description = description
        self.member_since = member_since
        self.last_updated = last_updated
        self.click_count = click_count

    def __repr__(self):
        return '<User %r>' % self.link


class User(UserMixin, db.Model):
    __tablename__  = 'users'
    id             = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username       = db.Column(db.String(64), unique=True, index=True, )
    password_hash  = db.Column(db.String(128))
    welcomeMessage = db.Column(db.Text())
    aboutme        = db.Column(db.Text())
    pgp            = db.Column(db.Text())
    pin            = db.Column(db.String(64))
    member_since   = db.Column(db.DateTime(), default=datetime.utcnow)
    email          = db.Column(db.String(128))


    def __init__(self, username, password, welcomeMessage, aboutme, pgp, pin, member_since, email):
        self.username = username
        self.password = password
        self.welcomeMessage = welcomeMessage
        self.aboutme = aboutme
        self.pgp = pgp
        self.pin = pin
        self.member_since = member_since
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username


    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def reset_password(self, token, new_password):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('reset') != self.id:
            return False
        self.password = new_password
        db.session.add(self)
        return True


    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)



    def generate_auth_token(self, expiration):
        s = Serializer(current_app.config['SECRET_KEY'],
                       expires_in=expiration)
        return s.dumps({'id': self.id}).decode('ascii')

    def confirm(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('confirm') != self.id:
            return False
        self.confirmed = True
        db.session.add(self)
        return True

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return None
        return User.query.get(data['id'])




class AnonymousUser(AnonymousUserMixin):
    def can(self):
        return False

    def is_administrator(self):
        return False

login_manager.anonymous_user = AnonymousUser


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

