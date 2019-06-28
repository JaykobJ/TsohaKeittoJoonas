from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators, ValidationError


class PersonForm(FlaskForm):
    name = StringField("Name", [validators.DataRequired()])
    email = StringField("Email address", [validators.DataRequired(), validators.Email(message='Invalid email')])
    address = StringField("Street address", [validators.DataRequired()])

    class Meta:
        csrf = False