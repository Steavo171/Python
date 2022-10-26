def div (a,b):                   #original function to divide two numbers
    print(a/b)


def smart_div(func):            #decorator #function are being passed as an argument as functions are an object in python
    def inner(a,b):                         #new function which modifies the existing function
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner


div = smart_div(div)         #assigning 2 functions (new function and old function)
div(2,4)    #calling the modified new function
# Code by Steavo Babu
