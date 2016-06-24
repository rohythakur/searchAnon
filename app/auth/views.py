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
    randompicture = ['numbers1.jpg', 'numbers2.jpg']

    picture = '/recaptcha/' + str((random.choice(randompicture)))
    print picture

    if str(picture) == '/recaptcha/numbers1.jpg':

        flash('numbers1111.jpg')
        recaptchaanswer = 11111
        flash("works11111111")
    if str(picture) == '/recaptcha/numbers2.jpg':
        flash('numbers22222.jpg')
        flash("works!!!222")
        recaptchaanswer = 11111
        if request.method == 'POST':
            flash('post test')
            print recaptchaanswer
            print str(RegistrationForm.recaptcha)
            if RegistrationForm.recaptcha == recaptchaanswer:
                flash('recaptcha works!')

                if form.validate_username():
                    flash('username test')



                    flash('recaptcha passed')
                    flash('Registered Successfully')
                    print "step 2 register"
                    user = User(username=form.username.data,
                                password=form.password.data,
                                welcomeMessage='',
                                aboutme = '',
                                pgp = '',
                                pin = '',
                                member_since = timestamp,
                                email = ''
                                )

                    db.session.add(user)
                    print "step 3 register"
                    db.session.commit()


                    flash('Registered Successfully')
                    return redirect(url_for('auth.login'))

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
