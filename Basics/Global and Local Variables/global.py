#to demonstrate the working to global variables
a=10
b=7
c=5
f=0
def sample():
    x=2

f=globals()['a']  # 'globals' will refer to all the global variables in the code unless specified by []
print(f)        #will print 10


a=10
def something():
    global a         #a variable in a function can be converted from local to global using global keyword
    a=15
    print("in function",a)

something()

print("outside",a)

#Code by Steavo Babu 
