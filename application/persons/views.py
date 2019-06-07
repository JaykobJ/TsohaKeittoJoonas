from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user
from application.persons.models import Person
from application.persons.forms import PersonForm

@app.route("/persons/information/")
@login_required
def persons_form():
    return render_template("persons/information.html", form=PersonForm())


@app.route("/persons/", methods=["POST"])
@login_required
def persons_create():
    form = PersonForm(request.form)

    if not form.validate():
        return render_template("recipes/new.html", form=form)

    r = Person(form.email.data, form.address.data, form.number.data)

    r.account_id = current_user.id

    db.session().add(r)
    db.session().commit()

    return redirect(url_for("index"))
