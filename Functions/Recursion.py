# Recursion - Recursion refers to the calling of same function by itself

import sys      #sys is a module
print(sys.getrecursionlimit())          #this function is used to determine the recursion limit 
                                                        #by default recursion limit is 1000 

sys.setrecursionlimit(1001)             #this function is used to change/set the recursion limit

print(sys.getrecursionlimit())


def greet():    #function declared
    
    print("Hello")
    greet()         #function being called by itself in the scope of the same function

greet()

#Code by Steavo Babu
