from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import owner

class Show:
    def __init__(self,data):
        self.id = data["id"]
        self.title = data["title"]
        self.network = data["network"]
        self.release_date = data["release_date"]
        self.description = data["description"]
        self.owner_id = data["owner_id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

        self.owner = {}

    @staticmethod
    def validate_show(data):
        is_valid = True
        if len(data["title"]) < 3:
            flash("Title must be at least 3 characters.")
            is_valid = False
        if len(data["network"]) < 3:
            flash("Network must be at least 3 characters.")
            is_valid = False
        if len(data["description"]) < 3:
            flash("Description must be at least 3 characters.")
            is_valid = False
        if data["release_date"] == "":
            flash("Please enter a date for your show!")
            is_valid = False
        return is_valid

    @classmethod
    def create_show(cls,data):
        query = "INSERT INTO shows (title, network, release_date, description, created_at, updated_at, owner_id) VALUES (%(title)s, %(network)s, %(release_date)s, %(description)s, NOW(), NOW(), %(owner_id)s);"
        results = connectToMySQL("tvshow_schema").query_db(query,data)
        return results

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM shows LEFT JOIN owners ON shows.owner_id = owners.id;"
        results = connectToMySQL("tvshow_schema").query_db(query) 
        all_shows = []
        for row in results:
            show = cls(row)
            owner_data = {
                "id": row["owners.id"],
                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "email": row["email"],
                "password": row["password"],
                "created_at": row["owners.created_at"],
                "updated_at": row["owners.updated_at"]
            }
            show.owner = owner.Owner(owner_data)
            all_shows.append(show)
        return all_shows

    @classmethod
    def get_show_with_owner(cls, data):
        query = "SELECT * FROM shows LEFT JOIN owners ON shows.owner_id = owners.id WHERE shows.id = %(show_id)s;"
        results = connectToMySQL("tvshow_schema").query_db(query,data)
        show = cls(results[0])
        owner_data = {
            "id": results[0]["owners.id"],
            "first_name": results[0]["first_name"],
            "last_name": results[0]["last_name"],
            "email": results[0]["email"],
            "password": results[0]["password"],
            "created_at": results[0]["owners.created_at"],
            "updated_at": results[0]["owners.updated_at"]
        }
        show.owner = owner.Owner(owner_data)
        return show

    @classmethod
    def update_show_info(cls, data):
        query = "UPDATE shows SET title = %(title)s, network = %(network)s, release_date = %(release_date)s, description = %(description)s, updated_at = NOW() WHERE shows.id = %(id)s;"
        results = connectToMySQL("tvshow_schema").query_db(query,data)
        return

    @classmethod
    def delete_show(cls,data):
        query = "DELETE FROM shows WHERE id = %(show_id)s;"
        results = connectToMySQL("tvshow_schema").query_db(query,data)
        return