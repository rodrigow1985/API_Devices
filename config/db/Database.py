import mysql.connector
from dotenv import load_dotenv
import os
from __main__ import app

load_dotenv()  # take environment variables from .env.

class Database:
    def __init__(self):
        self._conn = mysql.connector.connect(
            host=os.getenv('MYSQL_HOST') or 'localhost',
            port=os.getenv('MYSQL_PORT') or 3306,
            user=os.getenv('MYSQL_USER') or 'root',
            password=os.getenv('MYSQL_ROOT_PASSWORD') or 'rodrigow',
            database=os.getenv('MYSQL_DB') or 'db_home-server'
            )
        self._cursor = self._conn.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    @property
    def connection(self):
        return self._conn

    @property
    def cursor(self):
        return self._cursor

    def commit(self):
        self.connection.commit()

    def close(self, commit=True):
        if commit:
            self.commit()
        self.connection.close()

    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())

    def callproc(self, name_stored_procedure, params=None):
        return self.cursor.callproc(name_stored_procedure, params or ())

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchall()
    
    def stored_procedure(self, name_stored_procedure, params=None):
        try:
            print(params)
            self.cursor.callproc(name_stored_procedure, params or ())
            for result in self.cursor.stored_results():
                print('result antes del fetch')
                print(result)
                return result.fetchall()
        except mysql.connector.Error as error:
            print("Failed to execute stored procedure: {}".format(error))
        finally:
            if (self._conn.is_connected()):
                self.cursor.close()
                self.close()
                print("MySQL connection is closed")