from flask_wtf import FlaskForm
from wtforms import StringField, validators, ValidationError
from application.ingredient.models import Ingredient


class IngredientForm(FlaskForm):
    name = StringField("Ingredient name", [validators.DataRequired()])

    def validate_name(form,field):
        name = Ingredient.query.filter_by(name=field.data).first()
        if name is not None:
            raise ValidationError(message='Ingredient all ready exist')

    class Meta:
        csrf = False