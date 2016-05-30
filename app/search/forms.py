from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length,  Regexp

class searchForm(Form):

    searchString = StringField('', validators=[
        DataRequired(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                          'Searches must have only letters, '
                                          'numbers, dots or underscores')])

    submit = SubmitField('Search')