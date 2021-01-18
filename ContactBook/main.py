#CREATTING table and columns with a primary key column in it
import mysql.connector
from savecontact import _savecontact
from destroy import destroy_table
from colored import fg, bg, attr
from infodisplay import display_all
from updatecontact import _updatecontact
from deletecontact import _deletecontact

#we can comment out a line of sql code after it has been executed to go along without repeating a particular set of code like creating database or table again

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'contact'
)
#DATABASE has been created hence we will use database here and do further coding, so we dont run CREATE DATABASE
#again and again

#MAIN MENU
print ("%s%sWELCOME TO VIRTUAL CONTACT BOOK%s" % (fg('red'), bg('white'), attr('reset')))
print('''
        1. SAVE A CONTACT
        2. UPDATE A CONTACT 
        3. SHOW ALL CONTACTS
        4. DELETE A CONTACT
        5. DELETE ALL CONTACTS
        6. SHOW ALL CONTACTS''')

#OPTION SELECT
_optionselect = input("ENTER OPTION:")
if _optionselect == "1":
    _savecontact()
'''
if _optionselect == 2 list all the contacts with id and select id to update or delete
WHERE command sql helps select a data with a filter of name or id or anything for that matter
'''
if _optionselect == "2":
    _updatecontact()
if _optionselect == "3":
    display_all()
if _optionselect == "4":
    _deletecontact()
if _optionselect == "5":
    destroy_table()
if _optionselect == "6":
    display_all()