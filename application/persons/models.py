from application import db
from application.models import Base
from sqlalchemy.sql import text
from flask_login import current_user
from flask import flash, redirect, url_for

class Person(Base):

    __tablename__ = "person"

    name = db.Column(db.String(99), nullable=False)
    email = db.Column(db.String(99), nullable=False)
    address = db.Column(db.String(99), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address
