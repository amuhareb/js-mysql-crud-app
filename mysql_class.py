import pymysql
from dotenv import load_dotenv
import os

class Mysql:
    def __init__(self, host, user, password, database, port, unix_socket=None):
        try:
            self.mydb = pymysql.connect(
                user=user,
                password=password,
                host=host,
                database=database,
                port=port,
                unix_socket=unix_socket
            )
            self.cursor = self.mydb.cursor()
        except pymysql.Error as err:
            print(f'MYSQL error while connecting to the database. Error: {err}')
    
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.mydb.close()

    def execute(self, query):
        print("Inside execute_mysql_query function")  # Debugging line
        try:
            print('Executing query:', query)
            self.cursor.execute(query)
        except pymysql.Error as err:
            print('Error executing query:', err)
            return str(err)
        if 'SELECT' in query.upper():
            print('Query executed successfully.')
            result = self.cursor.fetchall()
        else:
            try:
                print('Committing changes to the database.')
                self.mydb.commit()
            except pymysql.Error as err:
                print('Error committing changes to the database:', err)
                return str(err)
            result = ('Query executed successfully.')
        return result

    def get_table_schema(self, table_name):
        try:
            query = f"DESCRIBE {table_name}"
            result = self.execute(query)
            return result
        except:
            print(f"Error fetching schema for table '{table_name}'")
            return None
