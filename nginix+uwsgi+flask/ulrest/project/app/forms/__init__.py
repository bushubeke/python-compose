from flask_wtf import FlaskForm,Form
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField,PasswordField,DateField
from wtforms.validators import DataRequired,Email,AnyOf,EqualTo,ValidationError