import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'contact'
)

def display_all():
    mycursor = mydb.cursor()
    mycursor.execute('SELECT * FROM contactinfo')
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)
