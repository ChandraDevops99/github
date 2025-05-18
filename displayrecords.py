import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Chandra@123$",
database="mydatabase"
)
mycursor =mydb.cursor()

sql = "select*from customers" 
mycursor.execute(sql)

print(mycursor.rowcount, "select records from Customes")