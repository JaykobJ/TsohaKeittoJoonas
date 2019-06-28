from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators, TextAreaField, SelectMultipleField, widgets
from sqlalchemy.sql import text
from application import db
from application.ingredient.models import Ingredient


def get_ingredients():
    try:
        query = text("SELECT * FROM ingredient")
        response = db.engine.execute(query)
        ingredients = []
        if response is not None:
            for row in response:
                # print("\n")
                # print(type(row))
                # print(type(row[3]))
                # print("\n")
                ingredient = (row[3], row[3])
                ingredients.append(ingredient)
        return ingredients
    except:
        print("exception")
        ingredients = []
        return ingredients



class MultiCheckboxField(SelectMultipleField):
    widget = widgets.TableWidget(with_table_tag=True)
    option_widget = widgets.CheckboxInput()
    coerce = str

class RecipeForm(FlaskForm):
    name = StringField("Recipe name", [validators.Length(min=1, max=99)])
    ingredients = MultiCheckboxField("Ingredients", choices=get_ingredients())
    instruction = TextAreaField("Instruction", [validators.Length(min=1)], render_kw={'class': 'form-control'})
  
    class Meta:
        csrf = False

    @classmethod
    def new(cls):
        # Instantiate the form
        form = cls()

        # Update the choices for the agency field
        form.ingredients.choices = get_ingredients()
        return form