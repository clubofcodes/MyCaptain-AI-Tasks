import sys
import numpy as np
lst = []
n = int(input("Enter number of elements : "))
for i in range(0,n):
    lst.append(float(input()))
def arr_type(lst):
    arr = np.asfarray(lst)
    return arr
print("Array of float-type: ",arr_type(lst))
type = arr_type(lst)