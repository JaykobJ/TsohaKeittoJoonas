from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user
from application.recipes.models import Recipe
from application.recipes.forms import RecipeForm
from application.auth.models import User


@app.route("/recipes", methods=["GET"])
def recipes_index():
    return render_template("recipes/list.html",  liked_recipes=User.get_user_liked_recipes())


@app.route("/recipes/new/")
@login_required
def recipes_form():
    return render_template("recipes/new.html", form=RecipeForm())


@app.route("/recipes/<recipe_id>/", methods=["POST"])
@login_required
def recipes_set_good(recipe_id):

    r = Recipe.query.get(recipe_id)
    r.good = True
    db.session().commit()
  
    return redirect(url_for("recipes_index"))


@app.route("/recipes/", methods=["POST"])
@login_required
def recipes_create():
    form = RecipeForm(request.form)

    if not form.validate():
        return render_template("recipes/new.html", form=form)

    r = Recipe(form.name.data)
    r.good = form.good.data
    r.account_id = current_user.id
    print('----------------------------------------')
    print(form.name.data)
    print(form.good.data)
    print('----------------------------------------')
    print(r.account_id)
    print(r.date_created)
    print(r.date_modified)
    print(r.good)
    print(r.id)
    print(r.name)
    print('----------------------------------------')
    db.session().add(r)
    db.session().commit()
  
    return redirect(url_for("recipes_index"))
