import colored
from colored import stylize
from colored import fg, bg, attr

def _mainmenu():
        print('%s%s ROOM ADVENTURE %s' % (fg('blue'), bg('yellow'), attr('reset')))
        print("""ROOM
                     1
                     2
                     3
                     4 
           """)
        _room = int(input("SELECT ROOM:"))  #int() for changing var type permanemtly
        if _room > 4 or _room <= 0:
                print("%s%sDont act ovesmart....this isnt a joke%s" % (fg('red'),bg('yellow'), attr('reset')))
                _mainmenu()

#ROOM 1
        if _room == 1:
                print("%s%s Welcome to room 1 %s" % (fg("red"), bg("yellow"), attr("reset")))
#ROOM 2          
        if _room == 2:
                print("%s%s Welcome to room 2 %s" % (fg("red"), bg("yellow"), attr("reset")))
#ROOM 3
        if _room == 3:
                print("%s%s Welcome to room 3 %s" % (fg("red"), bg("yellow"), attr("reset")))
#ROOM 4
        if _room == 4:
                print("%s%s Welcome to room 4 %s" % (fg("red"), bg("yellow"), attr("reset")))

        