import mysql.connector

#DELETE TABLE
def destroy_table():
    mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'root',
        database = 'contact'
    )

    mycursor = mydb.cursor()
    sql = "DROP TABLE IF EXISTS contact"
    mycursor.execute(sql)
    print("CONTACTS DELETED!")