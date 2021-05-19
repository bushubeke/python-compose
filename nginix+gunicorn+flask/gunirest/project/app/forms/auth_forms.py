# from flask_wtf import FlaskForm,Form
# from flask_wtf.file import FileField, FileRequired
# from wtforms import StringField,PasswordField,DateField
# from wtforms.validators import DataRequired,Email,AnyOf,EqualTo,ValidationError
########################################################################
#from .models import User
##########################################################################
from . import *
"""
def check_unique(form,field):
    if User.query.filter_by(username=field.data).first():
        raise ValidationError(f'{field.data} already used username')
def check_email_unique (form,field):
    if User.query.filter_by(email=field.data).first():
        raise ValidationError(f'{field.data} already used username')
"""
##########################################################################

class RegisterForm(FlaskForm):
    class Meta:
        csrf = False
    username=StringField('User Name', validators=[DataRequired()])
    first_name=StringField('First Name', validators=[DataRequired()])
    middle_name=StringField('Middle Name', validators=[DataRequired()])
    last_name=StringField('Last Name', validators=[DataRequired()])
    email=StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired(),EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')
class TokenLoginForm(FlaskForm):
    class Meta:
        csrf = False
    email=StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', [DataRequired()])

class ResendConfirmation(FlaskForm):
    class Meta:
        csrf = False
    email=StringField('Email', validators=[DataRequired(),Email()])

class ChangePassword(FlaskForm):
    class Meta:
        csrf = False
    password = PasswordField('Password', validators=[DataRequired(),EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')
class UpdateUserForm(FlaskForm):
    class Meta:
        csrf = False
    username=StringField('User Name', validators=[DataRequired()])
    first_name=StringField('First Name', validators=[DataRequired()])
    middle_name=StringField('Middle Name', validators=[DataRequired()])
    last_name=StringField('Last Name', validators=[DataRequired()])
    email=StringField('Email', validators=[DataRequired(),Email()])
class RemoveUserForm(FlaskForm):
    class Meta:
        csrf = False
    email=StringField('Email', validators=[DataRequired(),Email()])

class RoleForm(FlaskForm):
    class Meta:
        csrf = False
    name=StringField('Name',validators=[DataRequired()])
    description=StringField('Description',validators=[DataRequired()])
class UpadateRoleForm(FlaskForm):
    class Meta:
        csrf = False
    name=StringField('Name',validators=[DataRequired()])
    description=StringField('Description',validators=[DataRequired()])
class RemoveRoleForm(FlaskForm):
    class Meta:
        csrf = False
    name=StringField('Name',validators=[DataRequired()])
   
