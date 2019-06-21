from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators, ValidationError
from application.auth.models import User


class LoginForm(FlaskForm):
    username = StringField("Username", [validators.DataRequired()])
    password = PasswordField("Password", [validators.DataRequired()])

    class Meta:
        csrf = False


class RegisterForm(FlaskForm):
    name = StringField("Name", [validators.DataRequired()])
    username = StringField("Username", [validators.DataRequired()])
    def validate_username (form,field):
        name = User.query.filter_by(username=field.data).first()
        if name is not None:
            raise ValidationError(message='Username is all ready taken')
    password = PasswordField("Password", [validators.Length(min=3, max=20), validators.DataRequired()])

    class Meta:
        csrf = False
