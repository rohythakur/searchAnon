from flask import render_template, redirect, url_for, g, flash, request, session
from flask.ext.login import logout_user, current_user, login_required, login_user
from . import main
from .forms import EditProfileForm
from .. import db
from ..models import User
from app import login_manager, app


from sqlalchemy.orm.exc import UnmappedInstanceError



@app.before_request
def before_request():
    g.user = current_user


def logout():
    # remove the username from the session if it's there
    try:
       g.user.authenticated = False
       flask_login.logout_user()

       session.pop(username, None)
       print ("sucessfully logged out")
    except UnmappedInstanceError:
       print ("failed logged out")
    return redirect(url_for('auth.login'))



@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])

def index():
    print 'Should be running this index'

    return render_template('index.html')












@main.route('/auth/index', methods=['GET', 'POST'])

def logout():
    # remove the username from the session if it's there
    logout_user()
    g.user.authenticated = False


    print ("sucessfully logged out")

    return redirect(url_for('auth.login'))














@main.route('/contact', methods=['GET', 'POST'])
@login_required
def contact():
    return render_template('main/contact.html', user=user)



