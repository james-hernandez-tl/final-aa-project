from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import DataRequired, ValidationError
from app.models import Folder
from flask_login import current_user

def folderExist(form,field):
    folder = Folder.query.filter(Folder.name == field.data, Folder.userId == current_user.id).first()
    if folder and not form.data["edited"]:
        raise ValidationError(f"You already have a folder named {field.data}")

def lengthCheck(form,field):
    if (len(field.data) > 225):
        raise ValidationError("Your description is too long")

def sameUser(form,field):
    if (current_user.id != field.data):
        raise ValidationError("Unauthorized")

class folderForm(FlaskForm):
    name = StringField("name",validators=[DataRequired(),folderExist])
    userId = IntegerField("userId",validators=[DataRequired(), sameUser])
    description = StringField("description", validators=[DataRequired(), lengthCheck])
    edited = BooleanField("edited", default = False)
