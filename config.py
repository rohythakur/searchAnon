__author__ = 'ed'
WTF_CSRF_ENABLED = False
SECRET_KEY = 'you-will-never-guess'
import os


basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')



SQLALCHEMY_TRACK_MODIFICATIONS = True

PER_PAGE = 10
CSS_FRAMEWORK = 'bootstrap3'
LINK_SIZE = 'sm'

# decide whether or not a single page returns pagination
SHOW_SINGLE_PAGE = False