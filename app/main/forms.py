from flask_wtf import Form
from wtforms import StringField, SubmitField, validators


class addlinkForm(Form):

    link = StringField('URL Link', [validators.Length(min=16, max=16)])
    submit = SubmitField('Update')





