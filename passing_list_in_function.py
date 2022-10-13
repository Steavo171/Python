
def count(lst):
    even =0
    odd=0

    for i in lst :
        if i%2==0:
            even+=1
        else:
            odd+=1

    return even,odd

lst=[2,44,53,43,3,32,23,34,32,324,2]
even,odd =count(lst)

print("even :{} odd: {}".format(even,odd))
