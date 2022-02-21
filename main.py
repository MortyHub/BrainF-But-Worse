import sys
import faulthandler


sys.setrecursionlimit(10**6)
faulthandler.enable()


values = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", 'd', "e", 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q' ,'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', "D", "E", "F", "G", "H", "I", "J", "K", "L", "M","N","O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

chars = ["+", "-", ".","/", "["]
digits = ["0","1", "2", "3", "4", "5", "6", "7", "8", "9"]

cellValue = 0

Result = ""

code = input("Input Code >> ")

onLoop = False

print(f""" 
-----------------------
Welcome to the better
version of Brain F.

Python Ran

{code}
-----------------------
\n
""")

ranSoFar = []

def main(f):
    global ranSoFar
    global Result
    global cellValue


    for i in f:
        if i not in digits:
            ranSoFar += i
        if i == chars[0]:
            cellValue += 1
        elif i == chars[1]:
            cellValue = cellValue - 1
        elif i == chars[2]:
            Result += values[cellValue]
            cellValue = 0
        elif i == chars[3]:
            print(Result)
        elif i == chars[4]:
            cellValue = 0
            break
        elif i in digits:
            for s in range(int(i)):
                copy(ranSoFar)

def copy(f):
    global Result
    global cellValue


    for i in f:
        
        if i == chars[0]:
            cellValue += 1
        elif i == chars[1]:
            cellValue = cellValue - 1
        elif i == chars[2]:
            Result += values[cellValue]
            cellValue = 0
        elif i == chars[3]:
            print(Result)
        elif i == chars[4]:
            cellValue = 0
            break
        
main(code)

    