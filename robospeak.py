import sys

# abcdefghijklmnopqrstuvwxyz
def FromNums(numarray):
    RetVal = ""
    for num in numarray:

        # lowercase alphabet mappings
        if num == [0, 0, 0, 0,]:
            RetVal += "a"
        elif num == [0, 0, 0, 1]:
            RetVal += "b"
        elif num == [0, 0, 0, 2]:
            RetVal += "c"
        elif num == [0, 0, 0, 3]:
            RetVal += "d"
        elif num == [0, 0, 1, 0]:
            RetVal += "e"
        elif num == [0, 0, 1, 1]:
            RetVal += "f"
        elif num == [0, 0, 1, 2]:
            RetVal += "g"
        elif num == [0, 0, 1, 3]:
            RetVal += "h"
        elif num == [0, 0, 2, 0]:
            RetVal += "i"
        elif num == [0, 0, 2, 1]:
            RetVal += "j"
        elif num == [0, 0, 2, 2]:
            RetVal += "k"
        elif num == [0, 0, 2, 3]:
            RetVal += "l"
        elif num == [0, 0, 3, 0]:
            RetVal += "m"
        elif num == [0, 0, 3, 1]:
            RetVal += "n"
        elif num == [0, 0, 3, 2]:
            RetVal += "o"
        elif num == [0, 0, 3, 3]:
            RetVal += "p"
        elif num == [0, 1, 0, 0]:
            RetVal += "q"
        elif num == [0, 1, 0, 1]:
            RetVal += "r"
        elif num == [0, 1, 0, 2]:
            RetVal += "s"
        elif num == [0, 1, 0, 3]:
            RetVal += "t"
        elif num == [0, 1, 1, 0]:
            RetVal += "u"
        elif num == [0, 1, 1, 1]:
            RetVal += "v"
        elif num == [0, 1, 1, 2]:
            RetVal += "w"
        elif num == [0, 1, 1, 3]:
            RetVal += "x"
        elif num == [0, 1, 2, 0]:
            RetVal += "y"
        elif num == [0, 1, 2, 1]:
            RetVal += "z"

        # WIP: special character mappings
        elif num == [3, 0, 0, 0]:
            RetVal += " "
        elif num == [3, 0, 0, 1]:
            RetVal += "?"
        elif num == [3, 0, 0, 2]:
            RetVal += "."
        elif num == [3, 0, 0, 3]:
            RetVal += "!"
        

        else:
            RetVal += "?"
    return RetVal
        
class NotDivisibleBy4(Exception):
    pass

class NotRobo(Exception):
    pass

def ToNum(string):
    if string.strip() == "beep":
        return 0
    elif string.strip() == "boop":
        return 1
    elif string.strip() == "bop":
        return 2
    elif string.strip() == "bleep":
        return 3
    else:
        raise NotRobo

def ToNums(string):
    RetVal = []
    if not len(string.split(" ")) % 4 == 0:
        raise NotDivisibleBy4
    i = 3
    while i <= len(string.split(" ")):
        RetVal += [[ToNum(string.split(" ")[i - 3]), ToNum(string.split(" ")[i - 2]), ToNum(string.split(" ")[i - 1]), ToNum(string.split(" ")[i])]]
        i += 4
    return RetVal
        

def ToRobo(string):
    RetVal = ""
    for char in string:
        if char == "a":
            RetVal += "beep beep beep beep "
        elif char == "b":
            RetVal += "beep beep beep boop "
        elif char == "c":
            RetVal += "beep beep beep bop "
        elif char == "d":
            RetVal += "beep beep beep bleep "
        elif char == "e":
            RetVal += "beep beep boop beep "
        elif char == "f":
            RetVal += "beep beep boop boop "
        elif char == "g":
            RetVal += "beep beep boop bop "
        elif char == "h":
            RetVal += "beep beep boop bleep "
        elif char == "i":
            RetVal += "beep beep bop beep "
        elif char == "j":
            RetVal += "beep beep bop boop "
        elif char == "k":
            RetVal += "beep beep bop bop "
        elif char == "l":
            RetVal += "beep beep bop bleep "
        elif char == "m":
            RetVal += "beep beep bleep beep "
        elif char == "n":
            RetVal += "beep beep bleep boop "
        elif char == "o":
            RetVal += "beep beep bleep bop "
        elif char == "p":
            RetVal += "beep beep bleep bleep "
        elif char == "q":
            RetVal += "beep boop beep beep "
        elif char == "r":
            RetVal += "beep boop beep boop "
        elif char == "s":
            RetVal += "beep boop beep bop "
        elif char == "t":
            RetVal += "beep boop beep bleep "
        elif char == "u":
            RetVal += "beep boop boop beep "
        elif char == "v":
            RetVal += "beep boop boop boop "
        elif char == "w":
            RetVal += "beep boop boop bop "
        elif char == "x":
            RetVal += "beep boop boop bleep "
        elif char == "y":
            RetVal += "beep boop bop beep "
        elif char == "z":
            RetVal += "beep boop bop boop "

        # WIP: special character mappings
        elif char == " ":
            RetVal += "bleep beep beep beep "
        elif char == "?":
            RetVal += "bleep beep beep boop "
        elif char == ".":
            RetVal += "bleep beep beep bop "
        elif char == "!":
            RetVal += "bleep beep beep bleep "
        

        # return question mark if mapping not found
        else:
            RetVal += "bleep beep beep boop "
    return RetVal.strip()