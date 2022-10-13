#for else in python

nums=[14,34,43,34,56]

for num in nums :
    if num%5==0:
        print(num)
        break   #break is compulsory
else:           #this else doesnt comes under if statement , but comes under for loop
    print("not found")  #if no number is found in the list so instead of iterating over the if statement
                                #else statement can be used with respect to for
                                
