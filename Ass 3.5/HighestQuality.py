import pandas as pd
df=pd.read_csv("Thums up.csv",delimiter=';')
# print("Rows of Highest quality is :\n",df[df.quality == df.quality.max()])
print("Highest quality is :",df.quality.max())