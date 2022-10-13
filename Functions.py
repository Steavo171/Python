
#Types of arguments (Formal and Actual Parameters)

#Position 
def sum(a,b):  
    c=a+b
    print(c)
sum(5,6)    #the value 5 and 6 are passed to the variables a and b respectively by their position
print("------------")

#keyword
def person(name,age):
    print(name)
    print(age-5)
person(age=28,name='steavo')
print("---------")

#Default
def person (name ,age=18):
    print(name)
    print(age)
person('steavo')
print("-------------")
#Variable length argument #important


def sum(a,*b):       #here first value is alloted to a, then the remaining values are converted into a tuple and stored in b
    c=a             
    for i in b:         #for iterating throught the tuple beacuse a tuple and an integer variable cannot be added
        c=c+i
    print(c)
sum(3,3,4,4,5,56,8)

def sum(*b):   #it can also be written like this 
    c=0
    for i in b:
        c=c+i
    print(c)
sum(1,2,3,4,5,6,7,8,9,10)


    


'''
def add_sub(x,y):
    c=x+y
    d=x-y
    return c,d  #we can return more than one values in python

result1,result2=add_sub(5,4)
print(result1,result2)
#'''
