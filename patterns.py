
for r in range(5):
    for c in range(r):
        print("#",end=" ")   #end =" " is used such that the control wont go to the next line
    print()  #used for getting into new line // print("\n") can also be used 


for r in range(4):
    for c in range(r+1):
        print("#",end=" ") 
    print() 


for r in range(4,0,-1):           
    for c in range(r):              
        print("#",end=" ") 
    print()

#Code by Steavo Babu
