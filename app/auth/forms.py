from ..models import User
from flask_wtf import FlaskForm
from wtforms import PasswordField,StringField,SubmitField,ValidationError,BooleanField
from wtforms.validators import Required,EqualTo,Email


class RegistrationForm(FlaskForm):
  username=StringField("Enter username", validators=[Required()])
  email=StringField("Enter email",validators=[Required()])
  password=PasswordField("Password",validators=[Required(),EqualTo('password_confirm',message='Passwords must match')])
  password_confirm=PasswordField('Confirm password',validators=[Required()])
  submit=SubmitField('Sign Up')

  def validate_usermail(self,data_field):
    if User.query.filter_by(email=data_field.data).first():
      raise ValidationError("This email has been registered")
  
  def validate_username(self,data_field):
    if User.query.filter_by(username=data_field.data).first():
      raise ValidationError("This username is taken")

class LoginForm(FlaskForm):
  username=StringField("Enter username",validators=[Required()])
  password=PasswordField("Password",validators=[Required()])
  remember=BooleanField("Stay Logged in")
  submit=SubmitField("Log")
