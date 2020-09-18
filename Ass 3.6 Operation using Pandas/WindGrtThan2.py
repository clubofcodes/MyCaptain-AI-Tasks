import pandas as pd
df=pd.read_csv('forestfires.csv')
greater = df['wind'] > 2.0
print("Wind values greater than 2.0 are :\n",df.loc[greater,['wind']].sort_values('wind'))