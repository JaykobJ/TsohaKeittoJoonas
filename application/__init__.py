from flask import Flask
app = Flask(__name__)

# database connectivity and ORM
from flask_sqlalchemy import SQLAlchemy

import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///recipes.db"
    # Pyydetään SQLAlchemyä tulostamaan kaikki SQL-kyselyt
    app.config["SQLALCHEMY_ECHO"] = True

# DB object
db = SQLAlchemy(app)


from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager, current_user
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."

# roles in login_required
from functools import wraps


def login_required(accepted_roles=["USER", "ADMIN"]):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user:
                return login_manager.unauthorized()

            if not current_user.is_authenticated:
                return login_manager.unauthorized()

            unauthorized = False

            if accepted_roles != "ANY":
                unauthorized = True

                for user_role in current_user.roles():
                    for role in accepted_roles:
                        if user_role.name == role:
                            unauthorized = False
                            break

            if unauthorized:
                return login_manager.unauthorized()

            return fn(*args, **kwargs)

        return decorated_view

    return wrapper


#main views
from application import views
# recipes
from application.recipes import models
from application.recipes import views
# persons
from application.persons import models
from application.persons import views
# authenticator
from application.auth import models
from application.auth import views
# ingredients
from application.ingredient import models
from application.ingredient import views
# user recipes
from application.user_recipe import models
# recipe ingredients
from application.recipe_ingredient import models

# log in
from application.auth.models import User
from application.auth.models import Role

try:
    roles = Role.query.all()
    if len(roles) < 1:
        admin = Role(name="ADMIN")
        user = Role(name="USER")
        db.session().add(admin)
        db.session().add(user)
        db.session().commit()
        print("\n Roles added to table 'Roles' \n")
except:
    print("\n Could not add role to table 'Roles' \n")


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# creates tables to fb if necessary


try:
    db.create_all()
except:
    pass