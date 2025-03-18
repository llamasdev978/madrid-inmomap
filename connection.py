# pip install python-connector-mysql
import mysql.connector

db = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="1234"
)

print(db)