from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

class UserForm(FlaskForm):
    first_name = StringField('first_name', validators=[DataRequired()])
    last_name = StringField('last_name', validators=[DataRequired()])
    username = StringField('first_name', validators=[DataRequired()])
    password = PasswordField('last_name', validators=[DataRequired()])

class LoginForm(FlaskForm):
    username = StringField('first_name', validators=[DataRequired()])
    password = PasswordField('last_name', validators=[DataRequired()])
