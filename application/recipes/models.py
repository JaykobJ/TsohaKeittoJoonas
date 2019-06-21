from application import db
from application.models import Base
from sqlalchemy.sql import text
from application.auth.models import User


class Recipe(Base):

    __tablename__ = "recipe"
    
    name = db.Column(db.String(99), nullable=False)
    good = db.Column(db.Boolean, nullable=False)

    account = db.relationship("User", secondary="user_recipe", backref="Recipe")
    ingredient = db.relationship("Ingredient", secondary="recipe_ingredient", backref="Recipe")

    def __init__(self, name, good):
        self.name = name
        self.good = good


    @staticmethod
    def get_recipes():
        query = Recipe.query.filter(Recipe.account).all()
        recipes = []
        print("\n")
        print("--------------------")
        for o in query:
            print(len(query))
            recipes.append({"name": o.name, "username": o.account[0].username})
        return recipes
