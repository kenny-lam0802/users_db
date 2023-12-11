from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User

@app.route("/")
def index():
    users = User.get_all_users()
    return render_template("view_users.html", all_users = users)

@app.route("/user")
def sign_up():
    return render_template("add_user.html")

@app.route("/new/user", methods = ["POST"])
def create_form():
    User.add_user(request.form)
    return redirect('/')

@app.route("/user/view/<int:user_id>")
def show_one_user(user_id):
    one_user = User.get_one_user_by_id(user_id)
    return render_template("show_user.html", one_user = one_user)

@app.route("/user/update/<int:user_id>")
def update_this_user(user_id):
    this_user = User.get_one_user_by_id(user_id)
    return render_template("update_form.html" , this_user = this_user)

@app.route("/update/user", methods = ["POST"])
def update():
    User.update_by_id(request.form)
    return redirect("/")

@app.route("/user/delete/<int:user_id>")
def delete(user_id):
    User.delete_by_id(user_id)
    return redirect("/")