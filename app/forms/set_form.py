from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import DataRequired, ValidationError
from app.models import Set
from flask_login import current_user

def setExist(form,field):
    set = Set.query.filter(Set.name == field.data, Set.userId == current_user.id).first()
    if set and not form.data["edited"]:
        raise ValidationError(f"You already have a set named {field.data}")

def lengthCheck(form,field):
    if (len(field.data) > 225):
        raise ValidationError("Your description is too long")

def sameUser(form,field):
    if (current_user.id != field.data):
        raise ValidationError("Unauthorized")


class setForm(FlaskForm):
    name = StringField("name", validators = [DataRequired(),setExist])
    description = StringField("description", validators = [lengthCheck])
    draft = BooleanField("draft", default = False)
    edited = BooleanField("edit", default = False)
    userId = IntegerField("userId",validators = [DataRequired(),sameUser])
