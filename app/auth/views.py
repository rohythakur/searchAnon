from flask import render_template, redirect, url_for, flash, request, session, g
from flask_login import current_user, logout_user, flash, login_user
from . import auth
from .. import db
from ..models import User
from .forms import ChangePasswordForm, RegistrationForm, RegistrationFormTwo, LoginForm, LoginFormTwo
from sqlalchemy.orm.exc import UnmappedInstanceError
import random
from datetime import datetime


timestamp = datetime.today()


@auth.before_request
def before_request():

    g.user = current_user


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
            if form.validate_recpatcha(form.picture):

                user = User.query.filter_by(username=form.username.data).first()
                if user is not None and user.verify_password(form.password_hash.data):
                    print "success"
                    login_user(user)
                    current_user.is_authenticated = True
                    print (user)
                    return redirect(url_for('index'))


            else:
                flash("Please retry Recaptcha")
                return redirect(url_for('auth.loginTwo'))


    return render_template('auth/login.html', form=form)

@auth.route('/logintwo', methods=['GET', 'POST'])
def loginTwo():
    form = LoginFormTwo(request.form)
    if request.method == 'POST' and form.validate_on_submit():
            if form.validate_recpatcha(form.picture):


                user = User.query.filter_by(username=form.username.data).first()
                if user is not None and user.verify_password(form.password_hash.data):
                    print "success"
                    login_user(user)
                    current_user.is_authenticated = True
                    print (user)
                    return redirect(url_for('index'))





            else:
                flash("Please retry Recaptcha")
                return redirect(url_for('auth.login'))

    return render_template('auth/logintwo.html', form=form)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)

    print "registyer"
    if request.method == 'POST' and form.validate_on_submit():

        if form.validate_recpatcha(form.picture):

            user = User(username=form.username.data,
                        password=form.password.data,
                        welcomeMessage='',
                        aboutme='',
                        pgp='',
                        email='',
                        member_since=timestamp,
                        pin='')
            db.session.add(user)

            db.session.commit()

            flash("Registered Succesfully")
            return redirect(url_for('auth.login'))
        else:
            flash("Please retry Recaptcha")
            return redirect(url_for('auth.registertwo'))

    return render_template('/auth/register.html', form=form)



@auth.route('/registertwo', methods=['GET', 'POST'])
def registertwo():
    print "page 2 register"
    form = RegistrationFormTwo(request.form)

    if request.method == 'POST' and form.validate():
            if form.validate_recpatcha(form.picture):

                user = User(username=form.username.data,
                            password=form.password.data,
                            welcomeMessage='',
                            aboutme='',
                            pgp='',
                            email='',
                            member_since=timestamp,
                            pin='')
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('auth.login'))
            else:

                flash("Please retry Recaptcha")
                return redirect(url_for('auth.register'))



    return render_template('/auth/registertwo.html', form=form)



##TODO ADD Recaptcha

@auth.route('/security/<username>', methods=['GET', 'POST'])
def security(username):
    form = ChangePasswordForm(request.form)
    user = User.query.filter_by(username=username).first()
    print (str(user))
    if form.validate_on_submit():
         print (str(user))
         print "form validated"
         user = User.query.filter_by(username=username).first()
         if current_user.verify_password(form.old_password.data):


            current_user.password = form.password.data


            db.session.add(current_user)
            db.session.commit()
            flash('Password updated')

            return redirect(url_for('main.user', username=current_user.username))
         else:
             flash("old password wrong")
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
