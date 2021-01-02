import random
import colored
from colored import fg,bg,attr

def dice_throw():
    global x
    x = random.randrange(1,7)    #IMP: Here 1 is include and 7 is NOT
    print(x)

dice_throw()
if x == 6 or x == 4:
    print("%s%sWOW! You get one more chance!%s" % (fg('green'), bg('white'), attr('reset')))
    dice_throw()