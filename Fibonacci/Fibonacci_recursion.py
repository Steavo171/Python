def fibonacci(n):           #recursive function
    if n<=1:
        return n
    else:
        return (fibonacci(n-1)+fibonacci(n-2))              #recursion code  


terms=int(input("Enter the number of terms:"))
if terms<=0:
    print("Enter valid number!")
else:
    print("Fibonacci series")   
    for i in range (terms):
        print(fibonacci(i))

#Code by Steavo Babu
