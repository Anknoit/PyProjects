import mysql.connector
from colored import fg, bg, attr
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'contact'
)



def _savecontact():
    mycursor = mydb.cursor()
    _name = input("ENTER NAME: ")
    _number = input("ENTER CONTACT NUMBER: ")
    
    if len(_number) < 10 or len(_number) > 10: 
        print("Please enter a valid 10 digit number!")

    else:
        sql = "INSERT INTO contactinfo (name, number) VALUES(%s,%s)"
        val = (_name, _number)
        mycursor.execute(sql, val)
        
        mydb.commit()   #mydb.commit(). It is required to make the changes, otherwise no changes are made to the table.

        print(mycursor.rowcount, "RECORD INSERTED!")
        print("ID NUMBER:", mycursor.lastrowid)
        print("%s%sREMEMBER THE ID FOR FUTURE PURPOSE%s" % (fg('red'), bg('yellow'), attr('reset')))

