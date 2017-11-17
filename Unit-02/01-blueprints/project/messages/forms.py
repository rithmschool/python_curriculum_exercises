from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length

class MessageForm(FlaskForm):
    content = StringField('first_name', validators=[DataRequired(), Length(4)])
