import mysql.connector
from infodisplay import display_all

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'contact'
)

mycursor = mydb.cursor()

def _deletecontact():   #Creating a main function to include all the process of idselect
    def _deletecontact_function(idselect):                      #Creating a variable fumction
        mycursor.execute('DELETE FROM contactinfo WHERE id =%s', (idselect,))
        print("RECORD DELETED!")
        mydb.commit()                                           #This is how you get a user input variable inseide a SQL COMMAND

    display_all()
    idselect = input("\nENTER ID FROM THE LIST:")   #\n is used to skip a line
    _deletecontact_function(idselect)