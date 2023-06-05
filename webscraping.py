import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Satya@123"
)
print(db)