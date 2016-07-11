from flask_wtf import Form
from wtforms import StringField, SubmitField, validators
from wtforms.validators import DataRequired, Length,  Regexp, EqualTo
import random

randompicture = ['image1.png', 'image2.png', 'image3.png', 'image4.png', 'image5.png', 'image6.png',
                 'image7.png', ]
class addlinkForm(Form):

    link = StringField('URL Link', validators=[

     Length(min=16, max=16), Regexp('^[A-Za-z][A-Za-z0-9]*$', 0,
                                              'Onions must have only letters/numbers, '
                                              '')])

    picture = '/recaptcha/' + str((random.choice(randompicture)))

    recaptchaanswer = StringField('Please enter the letters from picture above ', validators=[
        DataRequired()])
    submit = SubmitField('Update')



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




