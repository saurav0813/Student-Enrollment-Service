import mysql.connector  # Use psycopg2 for PostgreSQL
from mysql.connector import Error

class Database:
    def __init__(self, config):
        self.config = config
        self.connection = self.create_connection()

    def create_connection(self):
        connection = None
        try:
            connection = mysql.connector.connect(**self.config)
            print("Connection to MySQL DB successful")
        except Error as e:
            print(f"The error '{e}' occurred")
        return connection

    def execute_query(self, query, data=None):
        cursor = self.connection.cursor()
        try:
            if data:
                cursor.execute(query, data)
            else:
                cursor.execute(query)
            self.connection.commit()
        except Error as e:
            print(f"The error '{e}' occurred")
        finally:
            cursor.close()

    def fetch_query(self, query, data=None):
        cursor = self.connection.cursor()
        result = None
        try:
            if data:
                cursor.execute(query, data)
            else:
                cursor.execute(query)
            result = cursor.fetchall()
        except Error as e:
            print(f"The error '{e}' occurred")
        finally:
            cursor.close()
        return result