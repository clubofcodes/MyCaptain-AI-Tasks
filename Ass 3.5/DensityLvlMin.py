import pandas as pd
df=pd.read_csv("Thums up.csv",delimiter=';')
print("Minimum density level is :",df.density.min())