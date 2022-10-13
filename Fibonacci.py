def fib(n):

    a=0
    b=1
    if n==0:
        print(0)
    elif(n<0):
        print("Enter valid number")
    else:
        a=0
        b=1
        print(a)
        print(b)

        for i in range(2,n):
            c=a+b
            a=b
            b=c
            print(c)

fib(5)




