from numpy import *     #module named numpy for mathematical operations
arr1 = array([
                    [1,2,3,4,5,6],
                    [3,4,5,6,7,8]

                    ])
print(arr1)
print(arr1.dtype) #it gives the data type of  the array (here it is int32)
print(arr1.ndim)  #it gives the dimention  of array it is
print(arr1.shape) #it gives the number of rows and coloumns
print(arr1.size) # if gives the size of the array i.e total number of elements
print(arr1.flatten()) # it would flatten the array that is convert from 2d to 1d array

arr2=arr1.reshape(3,4)  # (rows,columns) required
print(arr2)  

arr3=arr1.reshape(2,2,3) #it would create a 3d array , which will have two 2 d arrays and
                           # each 2d array would be having two 1d array which would be having 3 values each
            #reshape( two 2d array, two 1d array, three values in each 1d)
print(arr3)

#Code by Steavo Babu
