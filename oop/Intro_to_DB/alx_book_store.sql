import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="David6598@",
    database=""alx_book_store"
)

mycursor = mydb.cursor() 
mycursor.close()
mydb.close()