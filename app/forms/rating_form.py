from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import DataRequired, ValidationError
from app.models import Rating, Set
from .set_form import sameUser

def setExist(form,field):

    set = Set.query.get(field.data)

    if not set:
        raise ValidationError("set does not exist")

def lengthCheck(form, field):
    if 5 < field.data < 1 :
        raise ValidationError("Rating must be between 1 and 5")


class ratingForm(FlaskForm):
    userId = IntegerField("userId", validators = [DataRequired(), sameUser])
    setId = IntegerField("setId", validators = [DataRequired(), setExist])
    rating = IntegerField("rating", validators = [DataRequired(),lengthCheck])
