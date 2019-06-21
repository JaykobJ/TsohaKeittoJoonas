from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user
from application.persons.models import Person
from application.persons.forms import PersonForm


@app.route("/persons/information", methods=["GET", "POST"])
@login_required
def persons_information():

    if request.method == "GET":
        return render_template("persons/information.html", form=PersonForm())

    form = PersonForm(request.form)
    if request.method == "POST" and form.validate():
        info = Person(form.email.data, form.address.data, form.number.data)
        info.account_id = current_user.id
        db.session().add(info)
        db.session().commit()
        return redirect(url_for("index"))

    return render_template("persons/information.html", form=PersonForm())


@app.route("/persons/myinformation", methods=["GET", "POST"])
@login_required
def persons_myinformation_update():
    person_info = Person.query.get(current_user.id)

    if request.method == "GET":
        # fill form with user data
        if person_info is not None:
            updatedform = PersonForm()
            updatedform.email.data = person_info.email
            updatedform.address.data = person_info.address
            updatedform.number.data = person_info.number
            return render_template("persons/myinformation.html", form=updatedform)
        # blank form with no data
        return render_template("persons/myinformation.html", form=PersonForm())

    form = PersonForm(request.form)
    if request.method == "POST" and form.validate():
        if person_info is None:
            info = Person(form.email.data, form.address.data, form.number.data)
            info.account_id = current_user.id
            db.session().add(info)
        else:
            person_info.email = form.email.data
            person_info.address = form.address.data
            person_info.number = form.number.data
        db.session().commit()
        return redirect(url_for("index"))

    return render_template("persons/myinformation.html", form=PersonForm())