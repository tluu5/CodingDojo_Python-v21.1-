from crypt import methods
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.car import Car

@app.route("/new_car")
def new_car():
    if "owner_id" not in session:
        flash("Please login or register before entering the site!")
        return redirect("/")
    return render_template("new_car.html")

@app.route("/create_car", methods = ["POST"])
def create_car():
    data = {
        "price": request.form["price"],
        "model": request.form["model"],
        "make": request.form["make"],
        "year": request.form["year"],
        "description": request.form["description"],
        "owner_id": session["owner_id"]
    }
    if not Car.validate_car(data):
        return redirect("/new_car")
    Car.create_car(data)
    return redirect ("/dashboard")

@app.route("/car/<int:car_id>/show")
def show_car(car_id):
    if "owner_id" not in session:
        flash("Please login or register before entering the site!")
        return redirect("/")
    data = {
        "car_id": car_id
    }
    car = Car.get_car_with_owner(data)
    return render_template("show_car.html", car = car)

@app.route("/car/<int:car_id>/edit")
def edit_car(car_id):
    data = {
        "car_id" : car_id
    }
    car = Car.get_car_with_owner(data)
    return render_template("edit_car.html", car = car)

@app.route("/car/<int:car_id>/update", methods=["POST"])
def update_car(car_id):
    data = {
        "id": car_id,
        "price": request.form ["price"],
        "model": request.form ["model"],
        "make": request.form ["make"],
        "year": request.form ["year"],
        "description": request.form["description"],
        "owner_id": session ["owner_id"]
    }
    if not Car.validate_car(data):
        return redirect (f"/car/{car_id}/edit")
    Car.update_car_info(data)
    return redirect ("/dashboard")

@app.route("/car/<int:car_id>/delete")
def delete_car(car_id):
    data = {
        "car_id": car_id
    }
    Car.delete_car(data)
    return redirect("/dashboard")