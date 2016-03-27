from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length





class addlinkForm(Form):

    title = StringField('URL Title', validators=[Length(0, 64)])
    link = StringField('URL Link', validators=[Length(0, 64)])
    description = TextAreaField('Website Description')
    submit = SubmitField('Update')





