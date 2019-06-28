from application import app, db, login_required
from flask import redirect, render_template, request, url_for, flash
from flask_login import current_user
from application.persons.models import Person
from application.persons.forms import PersonForm


@app.route("/persons/information", methods=["GET", "POST"])
@login_required()
def persons_information():
    form = PersonForm(request.form)

    if request.method == "GET":
        return render_template("persons/information.html", form=form)

    if request.method == "POST" and form.validate():
        info = Person(form.name.data, form.email.data, form.address.data)
        info.account_id = current_user.id
        db.session().add(info)
        db.session().commit()
        return redirect(url_for("index"))

    return render_template("persons/information.html", form=form)


@app.route("/persons/myinformation", methods=["GET", "POST"])
@login_required()
def persons_myinformation_update():
    try:
        person_info = Person.query.get(current_user.id)
    except:
        flash("Could not connect to database")
        return redirect(url_for("error_page", message="Error connecting to database"))

    form = PersonForm(request.form)
    if request.method == "GET":
        # fill form with user data
        if person_info is not None:
            updatedform = PersonForm()
            updatedform.name.data = person_info.name
            updatedform.email.data = person_info.email
            updatedform.address.data = person_info.address
            return render_template("persons/myinformation.html", form=updatedform)
        # blank form with no data
        return render_template("persons/myinformation.html", form=form)

    form = PersonForm(request.form)
    if request.method == "POST" and form.validate():
        if person_info is None:
            try:
                info = Person(form.name.data, form.email.data, form.address.data)
                info.account_id = current_user.id
                db.session().add(info)
            except:
                flash("could not get account information")
                return redirect(url_for("error_page", message="Error connecting to database"))
        else:
            person_info.name = form.name.data
            person_info.email = form.email.data
            person_info.address = form.address.data
        try:
            db.session().commit()
        except:
            flash("Problems connecting to database")
            return redirect(url_for("error_page", message="Error connecting to database"))
        return redirect(url_for("index"))

    return render_template("persons/myinformation.html", form=form)

@app.route("/persons/delete_myinformation", methods=["POST"])
@login_required()
def delete_information():
    try:
        persons_info = Person.query.get(current_user.id)
        if persons_info is not None:
            db.session().delete(persons_info)
            db.session().commit()
            flash("Information deleted succesfully")
        else:
            flash("There is no information to delete")
        return redirect(url_for("persons_myinformation_update", form=PersonForm()))
    except:
        flash("Something went wrong")
