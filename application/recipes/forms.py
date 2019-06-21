from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators


class RecipeForm(FlaskForm):
    name = StringField("Recipe name", [validators.Length(min=1, max=99)])
    good = BooleanField("Good")
  
    class Meta:
        csrf = False