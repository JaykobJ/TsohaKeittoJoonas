from application import db
from application.models import Base
from sqlalchemy.sql import text


class User(Base):

    __tablename__ = "account"

    name = db.Column(db.String(99), nullable=False)
    username = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(30), nullable=False)

    recipes = db.relationship("Recipe", backref='account', lazy=True)
    person = db.relationship("Person", backref='account', lazy=True)

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

        
    @staticmethod
    def get_user_liked_recipes():
        query = text("SELECT Account.name, Recipe.name FROM Recipe"
                    " INNER JOIN Account ON Recipe.account_id = Account.id")
        result = db.engine.execute(query)
        good_recipes = []
        for row in result:
            good_recipes.append({"name": row[0], "recipe": row[1]})
        return good_recipes
