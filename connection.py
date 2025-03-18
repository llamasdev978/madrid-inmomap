# pip install python-connector-mysql
import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234"
)

print(db)