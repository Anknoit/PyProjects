print("LETS CREATE A STORY")
print("-----------------------------------")
val1 = input("Enter place for the story:")         #0
val2 = input("Enter the name of boy:")             #1
val3 = input("Enter the weapon: ")                 #2
val4 = input("Enter the sound of the weapon")      #3
val5 = input("Enter the name of girl:")            #4
val6 = input("Enter the name of villain:")         #5



#ERROR TIP: Replacement index 0 out of range for positional args tuple --- 0 is the array position of certain variable which need fixing so when putting variables inside format() for final print put according to arrays and dont miss any variable coz it can ruin the position/numbering of array


_place = val1.capitalize()
_boyname = val2.capitalize()
_weaponname = val3.capitalize()
_weaponsound = val4.capitalize()
_girlname = val5.capitalize()
_villainname = val6.capitalize()
print("--------------------------------------------------------------------------------")
story = """
            Once upon a time there was a place called {0}.
            A boy named {1} was one of the many residents in the village of {0}.
            He had a weapon which he called his {2} that made a sound {3} whenever it was 
            used. He was in love with a girl named {4} who was the daughter of {5} the cruel 
            ruler of the village. He defeated the cruel ruler and married his daughter and those
            fuckers lived happily ever after.
            THE END!
        """
print(story.format(_place, _boyname, _weaponname, _weaponsound, _girlname, _villainname))
