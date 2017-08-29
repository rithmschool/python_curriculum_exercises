from flask_wtf import FlaskForm
from wtforms import TextField, SelectMultipleField, widgets
from wtforms.validators import DataRequired
from project.models import Message


class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class TagForm(FlaskForm):
    text = TextField('Text',validators=[DataRequired()])
    messages = MultiCheckboxField('Messages',coerce=int)
    def set_choices(self):
        self.messages.choices = [(d.id, d.text) for d in Message.query.all()]

class DeleteTagForm(FlaskForm):
  # one way to handle CSRF in a delete form...
  pass
