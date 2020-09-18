import pandas as pd
df=pd.read_csv("Thums up.csv",delimiter=';')
df=df.reset_index()
print(df)