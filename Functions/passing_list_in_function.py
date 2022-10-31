
def count(lst):     
    even =0
    odd=0

    for i in lst :      #iterating through the loop
        if i%2==0:
            even+=1     #for counting even numbers
        else:
            odd+=1          #for counting odd numbers

    return even,odd

lst=[2,44,53,43,3,32,23,34,32,324,2]
even,odd =count(lst)  #two values being returned 

print("Even :{} Odd: {}".format(even,odd))

#Code by Steavo Babu
