from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired, Length,  Regexp, EqualTo
from ..models import User
from flask import flash
import random

randompicture = ['image1.png', 'image2.png', 'image3.png', 'image4.png', 'image5.png', 'image6.png',
                 'image7.png', ]
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


    picture = '/recaptcha/' + str((random.choice(randompicture)))
    print (str(picture))
    recaptchaanswer = StringField('Please enter the letters from picture abvove ', validators=[
        DataRequired()])
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


    def validate_recpatcha(self):


        picture = '/recaptcha/' + str((random.choice(randompicture)))
        print (str(picture))
        if str(picture) == '/recaptcha/image1.png':
            recaptchaa = 'CUXE'

            if recaptchaa == self.recaptchaanswer.data:
                return True
            else:
                return False

        if str(picture) == '/recaptcha/image2.png':
            recaptchaa = 'N3YS3'

            if recaptchaa == self.recaptchaanswer.data:
                return True
            else:
                return False
        if str(picture) == '/recaptcha/image3.png':
            recaptchaa = 'YKPU3U'

            if recaptchaa == self.recaptchaanswer.data:
                return True
            else:
                return False
        if str(picture) == '/recaptcha/image4.png':
            recaptchaa = 'YS4ARE'

            if recaptchaa == self.recaptchaanswer.data:
                return True
            else:
                return False
        if str(picture) == '/recaptcha/image5.png':
            recaptchaa = 'VCKR'

            if recaptchaa == self.recaptchaanswer.data:
                return True
            else:
                return False
        if str(picture) == '/recaptcha/image6.png':
            recaptchaa = 'YC3P'

            if recaptchaa == self.recaptchaanswer.data:
                return True
            else:
                return False
        if str(picture) == '/recaptcha/image7.png':
            recaptchaa = 'U64YW'


            if recaptchaa == self.recaptchaanswer.data:
                return True
            else:
                return False


class RegistrationFormTwo(Form):
    username = StringField('Username', validators=[
        DataRequired(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                              'Usernames must have only letters, '
                                              'numbers, dots or underscores')])
    password = PasswordField('Password', validators=[
        DataRequired(), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])

    welcomeMessage = StringField('Welcome Message', [validators.Length(min=10, max=64)])

    pin = (StringField('Enter your personal pin', [validators.Length(min=4, max=4)]))


    picture = '/recaptcha/' + str((random.choice(randompicture)))
    print (str(picture))
    recaptchaanswer = StringField('Please enter the letters from picture abvove ', validators=[
        DataRequired()])
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


    def validate_recpatcha(self):


        picture = '/recaptcha/' + str((random.choice(randompicture)))
        print (str(picture))
        if str(picture) == '/recaptcha/image1.png':
            recaptchaa = 'CUXE'

            if recaptchaa == self.recaptchaanswer.data:
                return True
            else:
                return False

        if str(picture) == '/recaptcha/image2.png':
            recaptchaa = 'N3YS3'

            if recaptchaa == self.recaptchaanswer.data:
                return True
            else:
                return False
        if str(picture) == '/recaptcha/image3.png':
            recaptchaa = 'YKPU3U'

            if recaptchaa == self.recaptchaanswer.data:
                return True
            else:
                return False
        if str(picture) == '/recaptcha/image4.png':
            recaptchaa = 'YS4ARE'

            if recaptchaa == self.recaptchaanswer.data:
                return True
            else:
                return False
        if str(picture) == '/recaptcha/image5.png':
            recaptchaa = 'VCKR'

            if recaptchaa == self.recaptchaanswer.data:
                return True
            else:
                return False
        if str(picture) == '/recaptcha/image6.png':
            recaptchaa = 'YC3P'

            if recaptchaa == self.recaptchaanswer.data:
                return True
            else:
                return False
        if str(picture) == '/recaptcha/image7.png':
            recaptchaa = 'U64YW'


            if recaptchaa == self.recaptchaanswer.data:
                return True
            else:
                return False
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


