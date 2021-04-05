# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 19:39:20 2020

@author: ANKIT JHA
"""
import random

"""
#ASSIGINING SHIT TO VARIABLE
"""
x, y, z = "Apple", "Orange", "Mango"
print(x)
print(y)
print(z)

a=b=c="Shit"
print(a+b+c)

#A string and an integer CANNOT be added together

"""
GLOBAL VARIABLE NAUTANKI
"""

m="Ankit"
print(m)
def myglobal():
        global m
        m = "Change"
        print(m)
myglobal() 
print(m)
       
global n
n="civic"
print(n)
def mydamnGlobal():
    n="What the f"
    print(n)
mydamnGlobal()
print(n)    

"""
DATA TYPES
"""

#know what type of variable it is by type()
_int = 5
_float= 5.0
_complex = 2j
_list = ['Rice', 'Chappati', 'daal']
_tuple = ("FLower", "trees", "Green")
_dict = {"Name":"Ankit", "Height":"6'", "Gender":"Male"}
_set = {"Dhoni","India","Cricket"}
_boolean = True
print(type(_int))
print(type(_float))
print(type(_complex))
print(type(_list))
print(type(_tuple))
print(type(_dict))
print(type(_set))
print(type(_boolean))

"""
NUMBER TYPES (like I care....)
"""
num = 3e4     #e represent power------>EXPONENT
print(num)


#CONVERTING NUMERICAL TYPES (Except complex number) 

i_num = float(23)
i_num2 = int(89.45)
i_num3 = complex(i_num)
print(i_num, i_num2, i_num3) #Dont add "+" sign while printing numbers

print(random.randrange(2,9)) #RANDOM NUMBER SHIT-----> import random


"""
STRINGS
"""

print("BOLLO BOLLO")
string_multiple = """My name is Ankit jha and 
                    I dont have any Idea what the
                    hell Iam doing here"""
                    #Line will break at points where you hit enter
print(string_multiple)

#PROOVING STRINGS ARE ARRAYS

txt = "Hello-Duniyawaalon"
print(txt[3])   #REMEMBER arrays start with 0
print(txt[2:5]) #SLICING - starting from left 
print(txt[-5:-3])
print(txt.strip())  #STRIP--Removes white spaces
print(txt.upper())  #upper()-- Makes everything uppercase
print(txt.lower())  #lower()-- Makes evrything lowercase
print(txt.replace("H","J"))     #replace()-- replace first alpha to second
print(txt.split("-"))           #split()-- split string ehrn it finds the char
                                #you want it to split from
                                
search_txt = "Duniya" in txt    #in --tells whether word is in txt by T/F
print(search_txt)   

search_txt2 = "Hello" not in txt#coz Hello is present=False
print(search_txt2)  
       
#format() method
itemno = 23       #[0]
price  = 300      #[1]
category= "toy"   #[2]
place = "bhilai"  #[3]
order = "Item number {} price: {} and category: {} is in bhilai:{}"
print(order.format(itemno, price, category, place))
#you can also place array number inside {} to assign that thing in a
#particular location you want
             
"""                                
Method	        Description

capitalize()	Converts the first character to upper case
casefold()	    Converts string into lower case
center()	    Returns a centered string
count()	        Returns the number of times a specified value occurs in a string
encode()	    Returns an encoded version of the string
endswith()	    Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	        Searches the string for a specified value and returns the position of where it was found
format()	    Formats specified values in a string
format_map()	Formats specified values in a string
index()	        Searches the string for a specified value and returns the position of where it was found
isalnum()	    Returns True if all characters in the string are alphanumeric
isalpha()	    Returns True if all characters in the string are in the alphabet
isdecimal()	    Returns True if all characters in the string are decimals
isdigit()	    Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	    Returns True if all characters in the string are lower case
isnumeric()	    Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	    Returns True if all characters in the string are whitespaces
istitle()	    Returns True if the string follows the rules of a title
isupper()	    Returns True if all characters in the string are upper case
join()	        Joins the elements of an iterable to the end of the string
ljust()	        Returns a left justified version of the string
lower()	        Converts a string into lower case
lstrip()	    Returns a left trim version of the string
maketrans()	    Returns a translation table to be used in translations
partition()	    Returns a tuple where the string is parted into three parts
replace()	    Returns a string where a specified value is replaced with a specified value
rfind()	        Searches the string for a specified value and returns the last position of where it was found
rindex()	    Searches the string for a specified value and returns the last position of where it was found
rjust()	        Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	    Splits the string at the specified separator, and returns a list
rstrip()	    Returns a right trim version of the string
split()	        Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()       	Returns a trimmed version of the string
swapcase()   	Swaps cases, lower case becomes upper case and vice versa
title()     	Converts the first character of each word to upper case
translate() 	Returns a translated string
upper()	        Converts a string into upper case
zfill()     	Fills the string with a specified number of 0 values at the beginning
"""



"""
BOOLEANS -  kya sach hai(T) or kya jhoot(F)
"""
#Almost any value is evaluated to True if it has some sort of content.

#Any string is True, except empty strings.

#Any number is True, except 0.

#Any list, tuple, set, and dictionary are True, except empty ones.
print(20>34)
print(43==43)
print(23<=30)
print(bool("ankit"))
bool_first = 34
print(bool(bool_first))
print(bool({}))

#VERIFYING WHETHER A SHIT IS A PARTICULAR DATATYPE -- isinstance()
wow=200
print(isinstance(wow, int))     #Checking whether "wow" is int


"""
OPERATORS---MATHEMATICAL SIGNS OF GOD
"""

#All sign are same except these two
# x**y --- x to the power y
# x//y --- y divides x and rounds the value to neares whole number

val = 3
val2 = 2
print(val**val2)
print(val//val2)

#IDENTITY OPERATORS
#is
#is not
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)

# returns True because z is the same object as x

print(x is y)

# returns False because x is not the same object as y, even if they have the same content

print(x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y




thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#This will return the items from position 2 to 5.

#Remember that the first item is position 0,
#and note that the item in position 5 is NOT included

print(thislist[:4]) #from first to 4th array

print(thislist[2:]) #from 2nd array to last array

thislist[2] = "Ankit" #cherry is now Ankit

print(thislist[2])
if "kiwi" in thislist:
    print("Yes, kiwi is in the list")
    
print(len(thislist))

thislist.append("lemon")    #will add lemon to the list in the END
print(thislist)

thislist.insert(3, "pattharchatta") #will add object at specific array location
print(thislist)

#REMOVING SHITS FROM LIST
thislist.remove("orange")   #removes a specified obj
print(thislist)

thislist.pop(4)             #removes a specified obj by array
print(thislist)             #if no array then it will remove last obj


#JOINING TWO LISTS
print(thislist+x)
"""
Method	    Description
-----------------------------------------------------
append()	Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()  	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position   
            list.insert(pos, elmnt)

pop()   	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()   	Sorts the list
            list.sort(reverse=True|False, key=myFunc)
            Parameter	Description
            reverse	Optional. reverse=True will sort the list descending. Default is reverse=False
            key	Optional. A function to specify the sorting criteria(s)
    sorted() -ascending arrangement, alphabetical arrangement
"""
_runnerup = [3,6,3,7,8,4,2,5]
_runnerup.sort()
_runnerup.append(17)
_runnerup.pop(2)                #Remove using element array position
_runnerup.remove(8)             #Remove using the element itself.....Numeric value without ""
_findpos = _runnerup.index(4)   #Find the position of specific element....string,number, list etc.
_runnerup.insert(3,"Waah Bhaiya") #Insert element in specific position
print("\nPosition of element:",_findpos)
print("\n",_runnerup)

"""
TUPLE
"""
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

"""
IF ELSE ELIF WHILE
"""

_var = 200
_var2 = 300

if _var > _var2:
    print("WTF")
elif _var<_var2:
    print("Jaaana be")
else:
    print("Chup")
    
if _var==_var2: print("WOEW")
print(_var) if _var < _var2 else print("_var2")

if _var == _var2:
    pass        # if CANNOT REMAIN EMPTY! Hence use "pass" to avoid err


#WHILE

i=0
while i<=60:
    print(i)
    i+=2
    if i == 30:
        break   #BREAK stops a loop even if the condition is true
    i+=2
    
j = 0
while j<=20:
    print(j)
    j+=2
    if j == 8:
        continue

k = 2
while k<=50:
    print(k)
    k+=2
else:
    print("K less than 50")

# DOCSTRING 
def definition(a):
    """
    Returns square of the value input
    """
    return a**2
help(definition)

#PRINTING characters in between 
print(1,2,3,4,5,6,7, sep="<")

#How to print in on line without any space
for n in range(0,15,3): # 3 is common difference
    print(n, end='')
#Return statements take conditions to return Booleans as well as other things as per the code

#LAMBDA
#takes any number of arguments but return one expression

_lam = lambda a,b,c: a*b*c
print(_lam(1,2,3))

#CLASSES/OBJECTS
class person:
    def __init__(self,name,age):  #3 arguments(object, info1,info2...)
        """
        The self Parameter
        The self parameter is a reference to the current instance of the class, 
        and is used to access variables that belongs to the class.

        It does not have to be named self , you can call it whatever you like, but it has to
        be the first parameter of any function in the class
        """
        self.name = name    
        self.age = age
    def _intro(self):
        print("HelLo, Motherfucks my name is " +self.name+" My age is "+self.age)

_man1 = person("Ankit", "20")
_man1._intro()
print(_man1.name)
print(_man1.age)

#PRINTING RUNNERUP SCORE OUT OF NUMEROUS SCORES
n = int(input())
arr = map(int, input().split())
print (sorted(set(arr))[-2])

