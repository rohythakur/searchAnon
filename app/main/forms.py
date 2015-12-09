from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, BooleanField, SelectField,\
    SubmitField, PasswordField, FileField, RadioField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError, validators
from ..models import User
from flask.ext.wtf import RecaptchaField
from flask.ext.babel import gettext


class ProfileviewForm(Form):

    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


class EditProfileForm(Form):

    location = StringField('Location', validators=[Length(0, 64)])
    about_me = TextAreaField('About me')

    welcomeM = StringField('Welcome Message', validators=[Length(0, 64)])
    pgpkey = TextAreaField('Pgp Key')
    submit = SubmitField('Update')





