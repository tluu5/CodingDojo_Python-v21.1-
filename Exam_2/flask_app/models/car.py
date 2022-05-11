from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import owner

class Car:
    def __init__(self,data):
        self.id = data["id"]
        self.price = data["price"]
        self.model = data["model"]
        self.make = data["make"]
        self.year = data["year"]
        self.description = data["description"]
        self.owner_id = data["owner_id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

        self.owner = {}

    @staticmethod
    def validate_car(data):
        is_valid = True
        if len(data["price"]) < 0:
            flash("Price must be greater than 0")
            is_valid = False
        if len(data["model"]) < 3:
            flash("Model must be at least 3 characters.")
            is_valid = False
        if len(data["make"]) < 3:
            flash("Make must be at least 3 characters.")
            is_valid = False
        if len(data["year"]) < 0:
            flash("Year must be greater than 0")
            is_valid = False
        if len(data["description"]) < 3:
            flash("Description must be at least 3 characters.")
            is_valid = False
        return is_valid

    @classmethod
    def create_car(cls,data):
        query = "INSERT INTO cars (price, model, make, year, description, created_at, updated_at, owner_id) VALUES (%(price)s, %(model)s, %(make)s, %(year)s, %(description)s, NOW(), NOW(), %(owner_id)s);"
        results = connectToMySQL("carshow_schema").query_db(query,data)
        return results

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM cars LEFT JOIN owners ON cars.owner_id = owners.id;"
        results = connectToMySQL("carshow_schema").query_db(query) 
        all_cars = []
        for row in results:
            car = cls(row)
            owner_data = {
                "id": row["owners.id"],
                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "email": row["email"],
                "password": row["password"],
                "created_at": row["owners.created_at"],
                "updated_at": row["owners.updated_at"]
            }
            car.owner = owner.Owner(owner_data)
            all_cars.append(car)
        return all_cars

    @classmethod
    def get_car_with_owner(cls, data):
        query = "SELECT * FROM cars LEFT JOIN owners ON cars.owner_id = owners.id WHERE cars.id = %(car_id)s;"
        results = connectToMySQL("carshow_schema").query_db(query,data)
        car = cls(results[0])
        owner_data = {
            "id": results[0]["owners.id"],
            "first_name": results[0]["first_name"],
            "last_name": results[0]["last_name"],
            "email": results[0]["email"],
            "password": results[0]["password"],
            "created_at": results[0]["owners.created_at"],
            "updated_at": results[0]["owners.updated_at"]
        }
        car.owner = owner.Owner(owner_data)
        return car

    @classmethod
    def update_car_info(cls, data):
        query = "UPDATE cars SET price = %(price)s, model = %(model)s, make = %(make)s, year = %(year)s, description = %(description)s, updated_at = NOW() WHERE cars.id = %(id)s;"
        results = connectToMySQL("carshow_schema").query_db(query,data)
        return

    @classmethod
    def delete_car(cls,data):
        query = "DELETE FROM cars WHERE id = %(car_id)s;"
        results = connectToMySQL("carshow_schema").query_db(query,data)
        return