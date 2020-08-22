import sys
import numpy as np
a = np.array([[[1,2,3],[4,5,6]],[[1,2,4],[2,3,6]],[[1,2,4],[2,3,6]]])
print(a)
print(a.ndim)

arr = np.array([[1,3,4],[1,3,3]])
print(arr.reshape(2,3)) #rowxcol=total element

a1=np.array([1,2,3,4])
print(a1[2])
a1=np.array([[1,2,3,4],[1,2,3,5]])
print(a1[0][2])

b = np.array([[1,2,3,4],[10,15,16,5],[1,2,4,5]])
print(b[0:,1])
print(b[0:,0:2])
print(b[1:2,0:2])