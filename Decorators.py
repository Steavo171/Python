def div (a,b):                    #original function
    print(a/b)


def smart_div(func):            #decorator
    def inner(a,b):                         #new function which modifies the existing function
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner


div = smart_div(div)         #assigning 2 functions (new function and old function)
div(2,4)    #calling the modiefied new function
