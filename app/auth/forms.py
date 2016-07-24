from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired, Length,  Regexp, EqualTo
from ..models import User
from flask import flash
import random
from sqlalchemy import func
randompicture = ['image1.png', 'image2.png', 'image3.png', 'image4.png', 'image5.png', 'image6.png',
                 'image7.png']



class RegistrationForm(Form):
    username = StringField('', validators=[
        DataRequired(), Length(7, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                          'Searches must have only letters, '
                                          'numbers, dots or underscores')])
    password = PasswordField('', validators=[
        DataRequired(), Length(7, 64), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('', validators=[DataRequired()])

    picture = '/recaptcha/' + str((random.choice(randompicture)))

    recaptchaanswer = StringField('Please enter the letters from picture abvove ', validators=[
        DataRequired()])


    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
    def validate(self):
        rv = Form.validate(self)
        if not rv:
            return False

        print "hello worlkd"
        username = User.query.filter(func.lower(User.username) == func.lower(self.username.data)).first()

        if username:
            self.username.errors.append("Invalid username or password")
            flash('username taken')
            return False
        else:
            print "doesnt work 1"

            return True


    def validate_recpatcha(self, picture):



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
    username = StringField('', validators=[
        DataRequired(), validators.Length(7, 25), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                              'Usernames must have only letters, '
                                              'numbers, dots or underscores')])
    password = PasswordField('', validators=[
        DataRequired(), EqualTo('', message='Passwords must match.')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])


    picture = '/recaptcha/' + str((random.choice(randompicture)))

    recaptchaanswer = StringField('Please enter the letters from picture above ', validators=[
        DataRequired()])


    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        rv = Form.validate(self)
        if not rv:
            return False


        username = User.query.filter(func.lower(User.username == self.username.data)).first()

        if username:
            print "Hello world again"
            self.username.errors.append("Invalid username or password")
            flash('username taken')
            return False
        else:
            print "doesnt work 2"

            return True


    def validate_recpatcha(self, picture):




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
        DataRequired(), Length(1, 25), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                          'Usernames must have only letters, '
                                          'numbers, dots or underscores')], description="test")
    password_hash = PasswordField('', validators=[ DataRequired()])
    picture = '/recaptcha/' + str((random.choice(randompicture)))

    recaptchaanswer = StringField('Please enter the letters from picture abvove ', validators=[
        DataRequired()])
    submit = SubmitField('Login')


    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        rv = Form.validate(self)
        if not rv:
            return False

        user = User.query.filter_by(username=self.username.data).first()
        if user and user.verify_password(self.password_hash.data):

            return True

        else:
            flash("Invalid username or password")
            #self.username.errors.append("Invalid username or password")
            return False

    def validate_recpatcha(self, picture):

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


class LoginFormTwo(Form):

    username = StringField('', validators=[
        DataRequired(), Length(7, 25), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                          'Usernames must have only letters, '
                                          'numbers, dots or underscores')], description="test")
    password_hash = PasswordField('', validators=[ DataRequired()])
    picture = '/recaptcha/' + str((random.choice(randompicture)))

    recaptchaanswer = StringField('Please enter the letters from picture abvove ', validators=[
        DataRequired()])
    submit = SubmitField('Login')


    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            print "wrong two"
            return False

        user = User.query.filter_by(username=self.username.data).first()
        if user and user.verify_password(self.password_hash.data):
            return True

        else:
            flash('invalid username or password')
            self.username.errors.append("Invalid username or password")
            return False

    def validate_recpatcha(self, picture):


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

class ChangePasswordForm(Form):
    old_password = PasswordField('Old password', validators=[DataRequired()])
    password = PasswordField('New password', validators=[
        DataRequired(), Length(7, 64),EqualTo('password2', message='Passwords must match')])
    password2 = PasswordField('Confirm new password', validators=[DataRequired()])
    picture = '/recaptcha/' + str((random.choice(randompicture)))

    recaptchaanswer = StringField('Please enter the letters from picture abvove ', validators=[
        DataRequired()])
    submit = SubmitField('Update Password')


    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)


    def validate_recpatcha(self, picture):
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