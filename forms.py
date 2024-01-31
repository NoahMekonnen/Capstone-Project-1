from random import choices
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, URLField, BooleanField,SelectField,IntegerField
from wtforms.validators import NumberRange

class PetForm(FlaskForm):