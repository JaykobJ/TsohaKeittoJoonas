from application import db
from application.models import Base
from sqlalchemy.sql import text


class RecipeIngredient(Base):

    __tablename__ = "recipe_ingredient"

    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'))
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient.id'))


    @staticmethod
    def get_recipe_ingredients(recipeid):
        try:
            query = text("SELECT ingredient.name"
                         " FROM ingredient, recipe_ingredient"
                         " WHERE recipe_ingredient.recipe_id = {}"
                         " AND ingredient.id = recipe_ingredient.ingredient_id".format(recipeid))
            response = db.engine.execute(query)
            ingredients = []
            for row in response:
                ingredients.append({"name": row[0]})
            return ingredients
        except Exception as e:
            return str(e)
