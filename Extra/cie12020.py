# import re
# p = re.compile('hello')
# r = p.match('hello everyone')
# print(r.group(0))
# r = re.match('hello', 'hello everyone')
# print(r.group(1))

# import numpy as np
# ary = np.array([1,2,3,5,8])
# ary = ary + 1
# print (ary[1])

# import numpy as np 
# import pandas as pd 
# # List of Tuples 
# matrix = [(10, 56, 17), 
#           (np.NaN, 23, 11), 
#           (49, 36, 55), 
#           (75, np.NaN, 34), 
#           (89, 21, 44) 
#           ] 
# # Create a DataFrame 
# abc = pd.DataFrame(matrix, index = list('abcde'), columns = list('xyz')) 
# # output  
# abc 
# maxValues = abc.max(axis = 0) 
# print(maxValues) 

# class Employee:
#     def __init__(self,first,last,pay): 
#         self.first = first
#         self.last = last
#         self.pay = pay
#     def __add__(self,other):
#         #missing code
#         return self.pay + other.pay
# emp1 = Employee("arjun","patel",700)
# emp2 = Employee("raj","joshi",900)
# print(emp1 + emp2)

# import numpy as np
# arr = np.array([ [1,2,3,4,5], [6,7,8,9,10] ])
# #missing code
# arr[:,4] = 11
# print(arr)

# import numpy as np
# arr = np.array([
# [[1,2],
# [3,4]],
# [[5,6],
# [7,8]],
# [[5,6],
# [7,8]]
# ])
# #missing code
# print(arr[2,:,1])

# import numpy as np
# arr1 = np.array([1,2,3,4,5])
# arr2 = arr1
# arr2[0] = 6
# print(arr1)

# class Test:
#     def __init__(self):
#         self.foo = 10
#         self._bar = 20
#         self.__baz = 30
# t = Test()
# print(t.foo)
# print(t._bar)
# #missing code
# print(t._Test__baz)