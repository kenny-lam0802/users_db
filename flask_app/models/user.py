from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__ (self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all_users(cls):
        query = "SELECT * from users;"
        results = connectToMySQL("users_schema").query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users
    
    @classmethod
    def add_user(cls, data):
        query = """INSERT into users(first_name, last_name, email)
                VALUES (%(first_name)s, %(last_name)s, %(email)s);
                """
        return connectToMySQL("users_schema").query_db(query, data)
    
    @classmethod
    def get_one_user_by_id(cls,id):
        query = """SELECT * from users
                WHERE id = %(id)s
                """
        results = connectToMySQL("users_schema").query_db(query, {"id":id})
        return cls(results[0])
    
    @classmethod
    def update_by_id(cls,data):
        query = """
                UPDATE users
                SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s
                WHERE id = %(id)s;
                """
        results = connectToMySQL("users_schema").query_db(query, data)
        return results
    
    @classmethod
    def delete_by_id(cls,id):
        query = """
                DELETE FROM users
                WHERE id = %(id)s;
                """
        results = connectToMySQL("users_schema").query_db(query, {"id":id})
        return results