import pandas as pd
df=pd.read_csv('forestfires.csv')
month = df['month']=='oct'
print("Temp values of oct month :\n",df.loc[month,['temp']])