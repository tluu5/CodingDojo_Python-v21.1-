from crypt import methods
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.show import Show

@app.route("/new_show")
def new_show():
    if "owner_id" not in session:
        flash("Please login or register before entering the site!")
        return redirect("/")
    return render_template("new_show.html")

@app.route("/create_show", methods = ["POST"])
def create_show():
    data = {
        "title": request.form["title"],
        "network": request.form["network"],
        "release_date": request.form["release_date"],
        "description": request.form["description"],
        "owner_id": session["owner_id"]
    }
    if not Show.validate_show(data):
        return redirect("/new_show")
    Show.create_show(data)
    return redirect ("/dashboard")

@app.route("/show/<int:show_id>/show")
def show_show(show_id):
    if "owner_id" not in session:
        flash("Please login or register before entering the site!")
        return redirect("/")
    data = {
        "show_id": show_id
    }
    show = Show.get_show_with_owner(data)
    return render_template("show_show.html", show = show)

@app.route("/show/<int:show_id>/edit")
def edit_show(show_id):
    data = {
        "show_id" : show_id
    }
    show = Show.get_show_with_owner(data)
    return render_template("edit_show.html", show = show)

@app.route("/show/<int:show_id>/update", methods=["POST"])
def update_show(show_id):
    data = {
        "id": show_id,
        "title": request.form ["title"],
        "network": request.form ["network"],
        "release_date": request.form ["release_date"],
        "description": request.form["description"],
        "owner_id": session ["owner_id"]
    }
    if not Show.validate_show(data):
        return redirect (f"/show/{show_id}/edit")
    Show.update_show_info(data)
    return redirect ("/dashboard")

@app.route("/show/<int:show_id>/delete")
def delete_show(show_id):
    data = {
        "show_id": show_id
    }
    Show.delete_show(data)
    return redirect("/dashboard")