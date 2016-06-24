from flask import render_template, redirect, url_for, flash, request, session, g
from flask_login import current_user, logout_user, flash, login_user
from . import auth
from .. import db
from ..models import User

from .forms import ChangePasswordForm, RegistrationForm, LoginForm
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
    randompicture = ['image1.png','image2.png','image3.png','image4.png','image5.png','image6.png','image7.png',]

    picture = '/recaptcha/' + str((random.choice(randompicture)))
    print picture

    if str(picture) == '/recaptcha/image1.png':

        recaptchaanswer = 'CUXE'

    if str(picture) == '/recaptcha/image2.png':

        recaptchaanswer = 'N3YS3'
    if str(picture) == '/recaptcha/image3.png':

        recaptchaanswer = 'YKPU3U'
    if str(picture) == '/recaptcha/image4.png':

        recaptchaanswer = 'YS4ARE'
    if str(picture) == '/recaptcha/image5.png':

        recaptchaanswer = 'VCKR'
    if str(picture) == '/recaptcha/image6.png':

        recaptchaanswer = 'YC3P'
    if str(picture) == '/recaptcha/image7.png':

        recaptchaanswer = 'U64YW'
        flash('post test')
        print recaptchaanswer
        print str(form.recaptcha.data)
    if request.method == 'POST':
        if form.recaptcha.data == recaptchaanswer:

                    flash('Registered Successfully')
                    return redirect(url_for('index'))
        else:
            flash("recaptcha is wrong")
            return redirect(url_for('auth.register'))

    return render_template('/auth/register.html', form=form, picture=picture)







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
