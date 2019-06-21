from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators


class PersonForm(FlaskForm):
    email = StringField("Email address", [validators.DataRequired(), validators.Email()])
    address = StringField("Street address", [validators.DataRequired()])
    number = StringField("Phone number", [validators.DataRequired()])

    class Meta:
        csrf = False