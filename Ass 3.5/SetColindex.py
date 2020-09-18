import pandas as pd
df=pd.read_csv("Thums up.csv",delimiter=';')
df=df.set_index("quality")
print(df)