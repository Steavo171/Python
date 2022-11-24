def stringcount(s):     #Defining a function for counting upper and lower case letters 
    L=0
    U=0
    for c in s :
        if c.islower():
            L+=1
        elif c.isupper():
            U+=1


    print("Lower case letter",L)
    print("upper case letter ",U)

s=str(input("Enter value"))
stringcount(s)      #Calling the function

#Code by Steavo Babu