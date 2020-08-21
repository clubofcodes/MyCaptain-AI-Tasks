import sys
import numpy as np
lst = []
n = int(input("Enter number of elements : "))
for i in range(0,n):
    lst.append(int(input()))
print("Numeric Value :",lst)
a = np.array(lst)
print("One-dimensional NumPy array: ",a)