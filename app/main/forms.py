from flask_wtf import Form
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


class addlinkForm(Form):

    link = StringField('URL Link', validators=[Length(16, 16)])
    submit = SubmitField('Update')





