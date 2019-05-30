from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators


class RecipeForm(FlaskForm):
    name = StringField("Recipe name", [validators.Length(min=2)])
    good = BooleanField("Good")
  
    class Meta:
        csrf = False