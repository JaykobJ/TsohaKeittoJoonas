from application import db
from application.models import Base
from sqlalchemy.sql import text


class User(Base):

    __tablename__ = "account"

    name = db.Column(db.String(99), nullable=False)
    username = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(30), nullable=False)

    recipe = db.relationship("Recipe", secondary="user_recipe", backref="Account")
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

    def roles(self):
        return ["ADMIN"]
