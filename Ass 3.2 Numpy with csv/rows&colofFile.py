import numpy as np
row_col = np.genfromtxt("Thums up.csv",delimiter=';',skip_header=1)
row=len(row_col[:])
col=len(row_col[0,:])
print("Total no. of rows = ",row)
print("Total no. of columns = ",col)