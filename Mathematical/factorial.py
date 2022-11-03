#to print the factorial of a given number
def factorial(n):
    
        fact=1
        for i in range(1,n+1):          #for looping 
            fact = fact*i
          
        return fact                     #returning the final value

num=int(input("Enter the number :"))
if num<0:                                                   #for negative integers
    print("Please enter a positive integer!")           
else:
    fact=factorial(num)
    print("Factorial of ",num, "is ",fact)

#Code by Steavo Babu
