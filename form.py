from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, BooleanField
from wtforms.validators import InputRequired, Optional, NumberRange,URL, AnyOf

class AddPetForm(FlaskForm):

    name=StringField("Pet Name")
    species=StringField("Species", validators=[AnyOf(values=["cat", "dog", "porcupine"], message='the species should be either “cat”, “dog”, or “porcupine”')])
    photo_url=StringField("Photo URL", validators=[Optional(),URL(message="It must be a Valid URL")])
    age=IntegerField("Age",validators=[NumberRange(min=0, max=30, message="Age should be between 0 and 30"), Optional()] )
    notes=StringField("Notes")
    


class EditPetForm(FlaskForm):

    photo_url=StringField("Photo URL", validators=[Optional(),URL(message="It must be a Valid URL")])
    notes=StringField("Notes")
    available=BooleanField("Available for Adoption?", default="checked" )

