import sys
import numpy as np
lst = []
n = int(input("Enter number of elements : "))
for i in range(0,n):
    lst.append(int(input()))
tup = tuple(lst)
alst = np.array(lst)
atup = np.array(tup)
print("List to array: ",alst)
print("Tuple to array: ",atup)