from application import db
from application.models import Base
from sqlalchemy.sql import text
from application.auth.models import User


class Recipe(Base):

    __tablename__ = "recipe"
    
    name = db.Column(db.String(99), nullable=False)
    instruction = db.Column(db.String(200), nullable=False)

    account = db.relationship("User", secondary="user_recipe", backref="Recipe")
    ingredient = db.relationship("Ingredient", secondary="recipe_ingredient", backref="Recipe")

    def __init__(self, name, instuction):
        self.name = name
        self.instruction = instuction

    @staticmethod
    def get_instructions(recipeid):
        try:
            query = text("SELECT recipe.name, recipe.instruction"
                         " FROM recipe"
                         " WHERE recipe.id = {}".format(recipeid))
            response = db.engine.execute(query).fetchone()
            recipe = {"name": response[0], "instruction": response[1]}
            return recipe
        except Exception as e:
            return str(e)

    @staticmethod
    def delete_recipe(recipeid):
        try:
            query = text("DELETE"
                         " FROM recipe, user_recipe, recipe_ingredient"
                         " WHERE recipe.id = {}"
                         " AND user_recipe.recipe_id = {}"
                         " AND recipe_ingredient.recipe_id = {}".format(recipeid, recipeid, recipeid))
            db.engine.execute(query)
            return "Recipe deleted succesfully"
        except Exception as e:
            return "Problems deleting recipe"

