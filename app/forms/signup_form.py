from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email, ValidationError
from app.models import User
import re


def user_exists(form, field):
    # Checking if user exists
    email = field.data
    user = User.query.filter(User.email == email).first()
    if user:
        raise ValidationError('email address is already in use.')

def checkUsername(form, field):
    username = field.data
    if (len(username) < 5):
        raise ValidationError("must contain at least 5 characters")
    if (len(username) > 50):
        raise ValidationError("must be under 50 characters")


def username_exists(form, field):
    # Checking if username is already in use
    username = field.data
    user = User.query.filter(User.username == username).first()
    if user:
        raise ValidationError('username is already in use.')


# def isImg(form, field):
#     image = field.data
#     valid = image.endswith((".png",".jpeg","jpg"))
#     if not valid :
#         raise ValidationError("Not a valid image")

def goodPassword(form,field):
    password = field.data
    if len(password) < 4:
        raise ValidationError("must be at least 4 characters")
    if not re.search("\d",password):
        raise ValidationError("password must contain a number")


def validEmail(form,field):
    email = field.data
    if not re.search("^[^@.]+@[^@]+\.[^@]+$",email):
        raise ValidationError("bad format; ex:james@email.com")


class SignUpForm(FlaskForm):
    username = StringField(
        'username', validators=[DataRequired(), username_exists, checkUsername])
    email = StringField('email', validators=[DataRequired(), user_exists,validEmail])
    password = StringField('password', validators=[DataRequired(),goodPassword])
