import mysql.connector
from infodisplay import display_all

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'contact'
)
mycursor = mydb.cursor()

def _updatecontact():   #Creating a main function to include all the process of idselect
    def _updatecontact_function(idselect):                      #Creating a variable fumction
        mycursor.execute('SELCT * FROM contactinfo WHERE id =%s', (idselect,))#This is how you get a user input variable inseide a SQL COMMAND

    display_all()
    idselect = input("\nENTER ID FROM THE LIST:")   #\n is used to skip a line
    _updatecontact_function(idselect)
'''

sql = "UPDATE customers SET address = %s WHERE address = %s"
val = ("Valley 345", "Canyon 123")
'''
