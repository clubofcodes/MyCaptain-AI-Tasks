import numpy as np
row_col = np.genfromtxt("Thums up.csv",delimiter=';',skip_header=1)
print("Fixed acidity :",row_col[:,0])
print("Average of fixed acidity :",np.average(row_col[:,0]))
print("Volatile acidity :",row_col[:,1])
print("Average of volatile acidity :",row_col[:,1])