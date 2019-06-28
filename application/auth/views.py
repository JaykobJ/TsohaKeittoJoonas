from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user

from application import app, db
from application.auth.models import User, Role
from application.auth.forms import LoginForm, RegisterForm


@app.route("/auth/login", methods=["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form=LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form=form,
                               error="No such username or password")

    login_user(user)
    return redirect(url_for("index"))


@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/auth/register", methods=["GET", "POST"])
def auth_register():
    if request.method == "GET":
        return render_template("auth/registerform.html", form=RegisterForm())

    form = RegisterForm(request.form)

    if request.method == "POST" and form.validate():
        try:
            new_user = User(form.username.data, form.password.data)
            user_role = Role.query.filter_by(id=2).first()
            #new_user.role.append(user_role)
            db.session().add(new_user)
            statement = User.account_role.insert().values(account_id=new_user.id, role_id=user_role.id)
            db.session.execute(statement)
            db.session().commit()
            user = User.query.filter_by(username=new_user.username, password=new_user.password).first()
            login_user(user)
            return redirect(url_for("persons_information"))
        except:
            flash("Error connecting to database", "error")
            return redirect(url_for("error_page", message="Error connecting to database"))

    return render_template("auth/registerform.html", form=form, error="Error creating account")
