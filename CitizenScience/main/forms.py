from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


from CitizenScience.models import Picture

class VerifyForm(FlaskForm):
    image_one=StringField('Image One')
    image_two=StringField('Image Two')    
    submit=SubmitField('Submit your choice')
