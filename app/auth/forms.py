from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired, Length,  Regexp, EqualTo
from ..models import User
from flask import flash


class RegistrationForm(Form):
    username = StringField('Username', validators=[
        DataRequired(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                              'Usernames must have only letters, '
                                              'numbers, dots or underscores')])
    password = PasswordField('Password', validators=[
        DataRequired(), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])

    welcomeMessage = StringField('Welcome Message', [validators.Length(min=10, max=64)])

    pin = (StringField('Enter your personal pin', [validators.Length(min=4, max=4)]))
    recaptcha = StringField('Please enter the letters from picture abvove ', validators=[
        DataRequired(), Length(5, 5), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                          'Recaptchas must have only letters, '
                                          'numbers, dots or underscores')])


    submit = SubmitField('Register')

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate_username(self):

            username = User.query.filter(User.username == self.username.data.lower()).first()
            print self.username.data.lower
            if username:
                # self.username.errors.append("Invalid username or password")
                flash('username taken')
                return False
            else:


                return True



class LoginForm(Form):

    username = StringField('', validators=[
        DataRequired(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                          'Usernames must have only letters, '
                                          'numbers, dots or underscores')], description="test")
    password_hash = PasswordField('', validators=[ DataRequired()])

    submit = SubmitField('Login')


    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False

        user = User.query.filter_by(username=self.username.data.lower()).first()
        if user and user.verify_password(self.password_hash.data):
            return True

        else:
            flash('invalid username or password')
            #self.username.errors.append("Invalid username or password")
            return False



class ChangePasswordForm(Form):
    old_password = PasswordField('Old password', validators=[DataRequired()])
    password = PasswordField('New password', validators=[
        DataRequired(), EqualTo('password2', message='Passwords must match')])
    password2 = PasswordField('Confirm new password', validators=[DataRequired()])
    welcomeM = StringField('Welcome Message', validators=[Length(1, 64)])
    submit = SubmitField('Update Password')


