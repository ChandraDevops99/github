import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Chandra@123$",
database="mydatabase"
)
mycursor =mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("chandra", "warangal 24")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")