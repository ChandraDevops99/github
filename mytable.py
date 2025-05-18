import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Chandra@123$"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")

import mysql.connector

mydb = mysql.connector.connect(
   host="localhost",
  user="root",
  password="Chandra@123$"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)