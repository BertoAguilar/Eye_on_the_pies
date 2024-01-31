from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from . import user

class Pie:
    db = "eye_on_the_pies"
    def __init__(self,data):
        self.id=data['id']
        self.name = data['name']
        self.filling = data['filling']
        self.crust = data['crust']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.baker = None
        self.creator = None

    @classmethod
    def save(cls, data):
        query= "INSERT INTO pies (users_id, name, filling, crust) VALUES (%(users_id)s, %(name)s, %(filling)s, %(crust)s)"
        return connectToMySQL(cls.db).query_db(query, data)

    @staticmethod
    def validate_pie(pie):
        is_valid = True
        query = "SELECT * FROM pies WHERE name= %(name)s;"
        results = connectToMySQL(Pie.db).query_db(query, pie)
        if len(results) >=1:
            flash("Pie name already exist", "createPie")
            is_valid=False
        if len(pie['name']) < 1:
            flash("Pie Is Missing A Name", "createPie")
            is_valid =False
        if len(pie['filling']) < 1:
            flash("Pie Is Missing Filling", "createPie")
            is_valid =False
        if len(pie['crust']) < 1:
            flash("Pie Is Missing Crust", "createPie")
            is_valid =False
        return is_valid

    @classmethod
    def get_all_pies(cls, data ):
        query = "SELECT * FROM pies JOIN users on users.id = pies.users_id;"
        results = connectToMySQL(cls.db).query_db(query, data)
        print(results)
        pies = []
        for row in results:
            pie = cls(row)
            all_pies_by_users = {
                'id': row['users.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'email': row['email'],
                'password': None,
                'created_at': row['users.created_at'],
                'updated_at': row['users.updated_at']
                }
            pie.baker=( user.User(all_pies_by_users) )
            pies.append(pie)
        return pies

    @classmethod
    def edit_pie(cls, data):
        query = "UPDATE pies SET name = '%(name)s', filling = '%(filling)s', crust = '%(crust)s' WHERE id=%(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def get_one_pies(cls, data ):
        query = "SELECT * FROM pies JOIN users on users.id = pies.users_id WHERE pies.id= %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        print(results)
        pies = []
        for row in results:
            pie = cls(row)
            all_pies_by_users = {
                'id': row['users.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'email': row['email'],
                'password': None,
                'created_at': row['users.created_at'],
                'updated_at': row['users.updated_at']
                }
            pie.creator=( user.User(all_pies_by_users) )
            pies.append(pie)
        return pies
    
    @classmethod
    def destroy_pie(cls, data):
        query= "DELETE FROM pies WHERE id= %(id)s)"
        return connectToMySQL(cls.db).query_db(query, data)
