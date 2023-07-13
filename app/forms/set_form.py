from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import DataRequired, ValidationError
from app.models import Set
from flask_login import current_user

def setExist(form,field):
    set = Set.query.filter(Set.name == field.data, Set.userId == current_user.id)
    if set:
        raise ValidationError(f"You already have a set named {field.data}")

def lengthCheck(form,field):
    if (len(field.data) > 225):
        raise ValidationError("Your description is too long")


class setForm(FlaskForm):
    name = StringField("name", validators = [DataRequired(),setExist])
    description = StringField("description", validators = [lengthCheck])
    draft = BooleanField("draft")
    userId = IntegerField("userId",validators = [DataRequired()])
