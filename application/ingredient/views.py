from application import app, db, login_manager, login_required
from flask import render_template, request, redirect, url_for, flash
from application.recipes.models import Recipe
from application.ingredient.models import Ingredient
from application.ingredient.forms import IngredientForm


@app.route("/ingredients", methods=["GET"])
@login_required()
def ingredient_index():
    return render_template("ingredient/list.html",  all_Ingredients=Ingredient.get_all_ingredients())


@app.route("/ingredients/new", methods=["GET", "POST"])
@login_required()
def ingredient_create():
    form = IngredientForm(request.form)
    if request.method == "GET":
        return render_template("ingredient/new.html", form=form)

    if request.method == "POST" and form.validate():
        try:
            ingredient = Ingredient(form.name.data)
            db.session().add(ingredient)
            db.session().commit()
        except:
            flash("could not connect to database")
            return redirect(url_for("error_page", message="Error connecting to database"))
        return redirect(url_for("ingredient_index"))

    return render_template("ingredient/new.html", form=form)
