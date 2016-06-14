from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, RadioField
from wtforms.validators import DataRequired, Length,  Regexp, EqualTo
from wtforms import ValidationError, validators
from ..models import User
from flask_wtf import RecaptchaField


class RegistrationForm(Form):

    username = StringField('Username', validators=[
        DataRequired(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                          'Usernames must have only letters, '
                                          'numbers, dots or underscores')])
    password = PasswordField('Password', validators=[
        DataRequired(), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])

    welcomeMessage = StringField('Welcome Message', validators=[Length(1, 64)])

    pin = (StringField('Enter your personal pin', validators=[Length(4, 4)]))
    submit = SubmitField('Register')


    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')


        username = User.query.filter(User.username == self.username.data.lower()).first()
        if username:

            self.username.errors.append("That username is already taken.")
            return False
        else:
          return True


#test