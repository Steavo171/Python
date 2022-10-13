from numpy import *
arr=array ([  [1,2,3],[4,5,6]  ])
print(arr)
print("----------------")
m=matrix(arr) # matrix function is inbuilt in numpy #one way of creating a matrix
print(m)  #ouput looks similar but we can perform certain operations
print("----------------")

# when input is taken from the user (second way of creating a matrix)
m=matrix('3,2;4,1')
print(m)
print("----------------")
m=matrix('3,2;4,1;1,3;7,7') # rows are separated from other rows by using a semicolon in between
print("----------------")
print(m)
print("----------------")
m1=matrix('1,2,3;4,5,6;7,8,9')
print(m1)
print("----------------")
print(diagonal(m1)) #inbuilt function used to print the diagonal values of a matrix
print(m1.min()) #prints min value in matrix
print(m1.max()) #prints max value in matrix
print("----------------")
m2=matrix('9,8,7;6,5,4;3,2,1')
m3=m1+m2 #matrix additon
print(m3)
print("----------------")
m4=m1*m2 #matrix multplication 
print(m4)




    

