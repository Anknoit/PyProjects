import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'contact'
)
mycursor = mydb.cursor()

print(mycursor)
# 1.CREATE DATABASE
'''
mycursor.execute("CREATE DATABASE contact")
print("DATABASE CREATED!")
'''

# 2.CREATE TABLE and ADD COLUMNS
'''
mycursor.execute("CREATE TABLE contactinfo (id INT AUTO_INCREMENT PRIMARY KEY, name varchar(255), number VARCHAR(255))")
print("TABLE CREATED WITH COLUMNS!")
print("READY TO GO")
'''