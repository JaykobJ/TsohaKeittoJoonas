import ast

from application import app, db, login_manager, login_required
from flask import render_template, request, redirect, url_for, flash
from flask_login import current_user
from application.recipes.models import Recipe
from application.recipes.forms import RecipeForm
from application.user_recipe.models import UserRecipe
from application.ingredient.models import Ingredient
from application.recipe_ingredient.models import RecipeIngredient
from application.auth.models import User


@app.route("/recipes", methods=["GET"])
@login_required()
def recipes_index():
    return render_template("recipes/list.html",  user_recipes=UserRecipe.get_user_recipes())


@app.route("/recipes/instructions/<recipe_id>")
@login_required()
def recipes_instructions(recipe_id):
    return render_template("recipes/recipe_view.html", recipe=Recipe.get_instructions(recipe_id),
                           ingredients=RecipeIngredient.get_recipe_ingredients(recipe_id))


@app.route("/recipes/delete/<recipeid>", methods=["POST"])
@login_required()
def delete_recipe(recipeid):
    print("\n\n MENEE DELETEEN \n\n")
    try:
        UserRecipe.query.filter_by(recipe_id=recipeid).delete()
        RecipeIngredient.query.filter_by(recipe_id=recipeid).delete()
        Recipe.query.filter_by(id=recipeid).delete()
        db.session().commit()
        flash(message="Recipe deleted succesfully", category="info")
        return redirect(url_for("recipes_index"))
    except:
        flash(message="There was a problem deleting recipe", category="error")
    return redirect(url_for("recipes_index"))


@app.route("/recipes/edit/<recipeid>", methods=["GET", "POST"])
@login_required()
def recipe_edit(recipeid):
    print("\n\n MENEE EDITEEN \n\n")
    try:
        recipe = Recipe.query.filter_by(id=recipeid).first()
        RecipeIngredient.query.filter_by(recipe_id=recipeid).delete()
        print("\n\n")
        print(recipe)
        print("\n\n")
    except:
        flash("Could not connect to database")
        return redirect(url_for("error_page", message="Error connecting to database"))

    form = RecipeForm().new()
    if request.method == "GET":
        print("\n\n MENEE gettiin \n\n")
        form.name.data = recipe.name
        form.instruction.data = recipe.instruction
        return render_template("recipes/edit.html", recipeid=recipeid, form=form)

    if request.method == "POST" and form.validate():
        print("\n\n MENEE postiin \n\n")
        recipe.name = form.name.data
        recipe.instruction = form.instruction.data
        for data in form.ingredients.data:
            ingredient = Ingredient.query.filter_by(name=data).first()
            recipe.ingredient.append(ingredient)
        try:
            print("\n\n COMMITOI \n\n")
            db.session().commit()
        except:
            flash("Problems connecting to database")
            return redirect(url_for("error_page", message="Error connecting to database"))
        return redirect(url_for("recipes_index"))

    return render_template("recipes/edit.html", recipeid=recipeid, form=form)


@app.route("/recipes/new", methods=["GET", "POST"])
@login_required()
def recipes_create():
    form = RecipeForm().new()
    if request.method == "GET":
        return render_template("recipes/new.html", form=form)

    if request.method == "POST" and form.validate():
        try:
            r = Recipe(form.name.data, form.instruction.data)
            r.account.append(current_user)

            for data in form.ingredients.data:
                ingredient = Ingredient.query.filter_by(name=data).first()
                r.ingredient.append(ingredient)
            db.session().add(r)
            db.session().commit()
            return redirect(url_for("recipes_index"))
        except:
            flash("could not connect to database")
            return redirect(url_for("error_page", message="Error connecting to database"))

    return render_template("recipes/new.html", form=form)
