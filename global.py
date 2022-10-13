a=10
b=7
c=5
f=0
def dd():
    x=2

fh=globals()['a']  #will refer to all the global variables in the code unless specified by []
print(fh)


'''
a=10
def something():
    global a
    a=15
    #a=15
    print("in function",a)

something()

print("outside",a)
'''
