from application import db
from application.models import Base


class Person(Base):

    email = db.Column(db.String(99), nullable=False)
    address = db.Column(db.String(99), nullable=False)
    number = db.Column(db.String(20), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    def __init__(self, email, address, number):
        self.email = email
        self.address = address
        self.number = number
