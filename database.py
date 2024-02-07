# database.py

import mysql.connector
from config import DATABASE_CONFIG

class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(**DATABASE_CONFIG)
        self.cursor = self.connection.cursor()

    def update_user(self, user_id, new_data):
        query = "UPDATE users SET name = %s, email = %s WHERE id = %s"
        values = (new_data['name'], new_data['email'], user_id)
        self.cursor.execute(query, values)
        self.connection.commit()

    def get_user(self, user_id):
        query = "SELECT id, name, email FROM users WHERE id = %s"
        self.cursor.execute(query, (user_id,))
        user_data = self.cursor.fetchone()
        if user_data:
            user_dict = {'id': user_data[0], 'name': user_data[1], 'email': user_data[2]}
            return user_dict
        else:
            return None

    def create_user(self, user_data):
        query = "INSERT INTO users (name, email) VALUES (%s, %s)"
        values = (user_data['name'], user_data['email'])
        self.cursor.execute(query, values)
        self.connection.commit()
        return self.cursor.lastrowid

    def close_connection(self):
        self.cursor.close()
        self.connection.close()
