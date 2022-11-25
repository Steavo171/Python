def fibonacci(n):

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

        for i in range(2,n):        #iterating till the number of terms
            c=a+b
            a=b
            b=c
            print(c)

n=int(input("Enter the number of terms :"))
fibonacci(n)

#Code by Steavo Babu


