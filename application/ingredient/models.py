from application import db
from application.models import Base
from sqlalchemy.sql import text


class Ingredient(Base):

    __tablename__ = "ingredient"

    name = db.Column(db.String(99), nullable=False)
    recipe = db.relationship("Recipe", secondary="recipe_ingredient", backref="Ingredient")

    def __init__(self, name):
        self.name = name

    @staticmethod
    def get_all_ingredients():
        query = text("SELECT * FROM Ingredient")
        result = db.engine.execute(query)
        ingredients = []

        for row in result:
            ingredients.append({"name": row[3]})
        return ingredients