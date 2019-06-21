from application import app, db, login_manager, login_required
from flask import render_template, request, redirect, url_for
from flask_login import current_user
from application.recipes.models import Recipe
from application.recipes.forms import RecipeForm
from application.auth.models import User


@app.route("/recipes", methods=["GET"])
def recipes_index():
    return render_template("recipes/list.html",  all_recipes=Recipe.get_recipes())


@app.route("/recipes/new/")
@login_required(role="ADMIN")
def recipes_form():
    return render_template("recipes/new.html", form=RecipeForm())


@app.route("/recipes/<recipe_id>/", methods=["POST"])
#@login_required
def recipes_set_good(recipe_id):

    r = Recipe.query.get(recipe_id)
    if r.account_id != current_user.id:
        # tee jotain, esim.
        return login_manager.unauthorized()
    r.good = True
    db.session().commit()
  
    return redirect(url_for("recipes_index"))


@app.route("/recipes/", methods=["POST"])
@login_required(role="ADMIN")
def recipes_create():
    form = RecipeForm(request.form)

    if not form.validate():
        return render_template("recipes/new.html", form=form)

    r = Recipe(form.name.data, form.good.data)
    r.account.append(current_user)
    db.session().add(r)
    db.session().commit()
  
    return redirect(url_for("recipes_index"))
