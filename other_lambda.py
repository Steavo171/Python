
from functools import reduce

doubles=[4,12,16,8,12,4]
sum1=reduce(lambda a,b:a+b,doubles)
print(sum1)

###########################################################################

def is_even(n):
    return n%2==0

nums=[9,99,8,8,467]
evens=list(filter(is_even,nums))
print(evens)



