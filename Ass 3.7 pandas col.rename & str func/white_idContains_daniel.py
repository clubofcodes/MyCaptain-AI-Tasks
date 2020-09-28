import pandas as pd
df=pd.read_csv('games.csv')
filt = df['white_id'].str.contains('daniel')
print("All The rows for whose white_id contains 'daniel' :\n",df.loc[filt,['id','white_id']])