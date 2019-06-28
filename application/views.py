from flask import render_template
from application import app
from application.user_recipe.models import UserRecipe


@app.route("/")
def index():
    return render_template("index.html", user_recipe_count=UserRecipe.get_user_recipes_count())


@app.route("/error/<message>")
def error_page(message):
    return render_template("errorpage.html", message=message)

