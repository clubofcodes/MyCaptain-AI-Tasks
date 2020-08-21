import sys
import numpy as np
# Initialize matrix 
lst = [] 
print("Enter the value row-wise : ") 
# For user input 
for i in range(0,9):
    lst.append(int(input())) 
    
def matrix(lst):
    matrix = np.array(lst).reshape(3,3)
    return matrix
print(matrix(lst))
dim = matrix(lst)
