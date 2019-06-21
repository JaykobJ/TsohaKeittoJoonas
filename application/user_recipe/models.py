from application import db
from application.models import Base


class UserRecipe(Base):

    __tablename__ = "user_recipe"

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'))
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'))
