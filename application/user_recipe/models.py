from application import db
from application.models import Base
from sqlalchemy.sql import text


class UserRecipe(Base):

    __tablename__ = "user_recipe"

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'))
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'))

    @staticmethod
    def get_user_recipes():
        query = text("SELECT recipe.id, recipe.name, account.username, account.id"
                     " FROM recipe, user_recipe, account"
                     " WHERE recipe.id = user_recipe.recipe_id"
                     " AND account.id = user_recipe.account_id"
                     " ORDER BY recipe.id")
        response = db.engine.execute(query)
        recipes = []
        for row in response:
            recipes.append({"recipe_id": row[0], "name": row[1], "username": row[2], "account_id": row[3]})
        return recipes

    @staticmethod
    def get_specified_user_recipes(user_id):
        query = text("SELECT recipe.id, recipe.name"
                     " FROM recipe, user_recipe"
                     " WHERE recipe.id = user_recipe.recipe_id"
                     " AND user_recipe.account_id = {}"
                     " ORDER BY recipe.id".format(user_id))
        response = db.engine.execute(query)
        recipes = []
        for row in response:
            recipes.append({"recipe_id": row[0], "recipe_name": row[1]})
        return recipes

    @staticmethod
    def get_user_recipes_count():
        query = text("SELECT account.username, COUNT (*) count"
                     " FROM account, recipe, user_recipe"
                     " WHERE account.id = user_recipe.account_id"
                     " AND recipe.id = user_recipe.recipe_id"
                     " GROUP BY account.id"
                     " ORDER BY Count(*) DESC")
        response = db.engine.execute(query)
        recipes_count = []
        for row in response:
            recipes_count.append({"username": row[0], "recipe_count": row[1]})
        return recipes_count