from flask.ext.wtf import Form
from wtforms.fields import TextField,SelectField,IntegerField
from wtforms.validators import Required 

from flask_wtf.file import FileField, FileAllowed, FileRequired
from app import db
from app.models import User


def age_validator(form , field):
    try:
        age = int(field.data)
        if not age in range(5,130):
            field.errors.append('Age is outside valid range')
            return False
        return True
    except TypeError:
        field.errors.append('Age must be an integer')
        return False

def image_file_validator(form , field):
    extension = field.data.filename.split('.')[-1].lower()
    if not extension in ('jpg' , 'jpeg' , 'png'):
        field.errors.append('Files must be either jpg or png format')
        return False
    return True

def unique_username_validator(form , field):
    user = db.session.query(User).filter_by(username=field.data).first()
    if user != None:
        field.errors.append('Username already taken')
        return False
    return True


class UserForm(Form):
    firstname = TextField('First Name' , validators=[Required()])
    lastname = TextField('Last Name' , validators=[Required()])
    username = TextField('Username' , validators=[unique_username_validator ,Required()])
    age = IntegerField('Age' , validators=[age_validator,Required()])
    sex = SelectField('Sex' , choices = [('male','Male') , ('female' , 'Female')])
    image = FileField('Profile Picture' , validators=[image_file_validator,Required()])


            

