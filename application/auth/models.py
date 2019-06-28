from application import db
from application.models import Base
from sqlalchemy.sql import text


class User(Base):

    __tablename__ = "account"

    username = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(30), nullable=False)

    recipe = db.relationship("Recipe", secondary="user_recipe", backref="Account")
    person = db.relationship("Person", backref='account', lazy=True)
    role = db.relationship('Role', secondary='account_role', backref='Account', lazy=True)

    def __init__(self, username, password):
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
        return self.role

class Role(Base):

    name = db.Column(db.String(144), nullable=False)

    account = db.relationship("User", secondary="account_role", backref="Role", lazy=True)

    def __init__(self, name):
        self.name = name


account_role = db.Table('account_role',
    db.Column('account_id', db.Integer, db.ForeignKey('account.id'), nullable=False),
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'), nullable=False))