import numpy as np
row_col = np.genfromtxt("Thums up.csv",delimiter=';',skip_header=1)
print("Residual sugar :",row_col[:,3])
print("Minimum residual sugar :",np.min(row_col[:,3]))