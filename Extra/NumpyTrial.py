import numpy as np
arr = np.array([
            [["Butki",2,"RahuKetu"],[1,2,3]],
            [["Dhingli",2,"Teddy"],[1,2,3]]
            ], ndmin=10)
# print(arr)
# print(arr.ndim)

arr2 = np.array([
            [[1,45,3],[1,2,1]],
            [[1,2,4],[2,56,7]],
            [[1,2,4],[2,56,7]]
                ])
x=np.arange(1,60,5)
# x=x.reshape(3,4)
# print(arr2[1:2,1:2,1:2]) #3d-slicing
print(arr2.ndim)
# print(arr2.itemsize)
# print(arr2.dtype)
# print(arr2.flags)
# print(np.resize(arr2,(8,3)))
# print(x)
# print(x.shape)
# print(x.reshape(3,4))
# print(arr2.shape)
# print(arr2.reshape(2,9))

# print(np.nditer(x)) ask for without forloop

a = np.arange(100000,dtype=int)
print(a.size)