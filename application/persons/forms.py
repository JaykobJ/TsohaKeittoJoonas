from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators


class PersonForm(FlaskForm):
    email = StringField("Email address")
    address = StringField("Street address")
    number = StringField("Phone number")

    class Meta:
        csrf = False