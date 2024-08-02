import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="David6598@",
    database="mydatabase"
)

print(mydb.get_server_info())   
