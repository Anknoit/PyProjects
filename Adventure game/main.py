"""
ROOM ADVENTURE 
"""
import colored
from colored import stylize
from colored import fg, bg, attr
#from mainmenu import *  -----> For importing all the modules 
from mainmenu import _mainmenu

_mainmenu()
def _name():
    _usr = input("ENTER YOUR NAME:")
    print("Hi", _usr.capitalize(),"!")
_name()

