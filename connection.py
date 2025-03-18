# pip install python-connector-mysql
import mysql.connector

class DbManager:
    def __init__(self, host="127.0.0.1", user="root", pwd="", db="inmomapbdd"):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=pwd,
            database=db,
        )

        self.cursor = self.connection.cursor()