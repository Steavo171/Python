a=5
b=6
# by using an extra variable
temp=a
a=b
b=temp
print (a)
print (b)

# other method; btw wasting an extra bit
a=a+b
b=a-b
a=a-b

#by XOR method

a=a^b
b=a^b
a=a^b

# (only in python)
a,b=b,a 

#Code by Steavo Babu
