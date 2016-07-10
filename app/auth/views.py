from flask import render_template, redirect, url_for, flash, request, session, g
from flask_login import current_user, logout_user, flash, login_user
from . import auth
from .. import db
from ..models import User
from .forms import ChangePasswordForm, RegistrationForm, RegistrationFormTwo, LoginForm
from sqlalchemy.orm.exc import UnmappedInstanceError
import random
from datetime import datetime


timestamp = datetime.today()


@auth.before_request
def before_request():
    #current_user.ping()
    g.user = current_user


@auth.route('/login', methods=['GET', 'POST'])
def login():
    ##TODO add recaptcva
    form = LoginForm(request.form)
    if request.method == 'POST':
        print 'Post'
        if form.validate_on_submit():

            user = User.query.filter_by(username=form.username.data).first()
            if user is not None and user.verify_password(form.password_hash.data):
                print "success"
                login_user(user)
                current_user.is_authenticated = True
                print (user)
                return redirect(url_for('index'))


            flash('Invalid username or password.')



    return render_template('auth/login.html', form=form)



@auth.route('/register', methods=['GET', 'POST'])
def register():
    ##TODO RECAPTCHA


    print "step 1 register"
    form = RegistrationForm(request.form)

    if request.method == 'POST':

        if form.validate_recpatcha():


            print ("Works?")
            flash('Registered Successfully')

            return redirect(url_for('index'))
        else:

            print ("wrong going to retry")
            return redirect(url_for('auth.registertwo'))

    return render_template('/auth/register.html', form=form)



@auth.route('/registertwo', methods=['GET', 'POST'])
def registertwo():
    ##TODO RECAPTCHA


    print "step 1 register"
    form = RegistrationFormTwo(request.form)

    if request.method == 'POST':

        if form.validate_recpatcha():


            print ("Works?")
            flash('Registered Successfully')

            return redirect(url_for('index'))
        else:
            print ("wrong going back to first")

            return redirect(url_for('auth.register'))

    return render_template('/auth/registertwo.html', form=form)





@auth.route('/security/<username>', methods=['GET', 'POST'])
def security(username):
    ##TODO add recaptcva
    form = ChangePasswordForm(request.form)
    user = User.query.filter_by(username=username).first()
    print ("here")
    if form.validate_on_submit():
         if current_user.verify_password(form.old_password.data):
            print ("info updated")
            user.password = form.password.data
            user.welcomeM = form.welcomeM.data

            db.session.add(user)
            db.session.commit()
            flash('Password updated')

            return redirect(url_for('main.user', username=current_user.username))
    return render_template('/auth/security.html', user=user, form=form)


@auth.route('/onions/<username>', methods=['GET', 'POST'])
def myonions(username):
    ##TODO add custom onions
    user = User.query.filter_by(username=username).first()
    return render_template('/auth/myonions.html', user=user)


@auth.route("/logout", methods=["GET"])
def logout():
    try:

        logout_user()

        print "logged out"
    except UnmappedInstanceError:
       pass
    return redirect(url_for('index'))
