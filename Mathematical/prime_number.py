#to check whether a number is prime or composite

num = int(input("Enter a number :")) # input
if num<0:       # condition for avoiding negative integers
    print("Enter a positive integer")
elif num== 0 or num==1:     # special cases
    print("The number is neither prime nor composite")
else:
    flag = True # boolean 

    for i in range(2,num):
        if num % i == 0:
            flag = False
            break
  
    if flag == True:
        print(num," is a Prime Number")
    else:
       print(num," is a Composite number")

#Code by Steavo Babu
