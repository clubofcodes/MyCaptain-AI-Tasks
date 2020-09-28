import pandas as pd
df=pd.read_csv('games.csv')
filt = df['black_id'].str.startswith('sh') 
print("All The rows for whose black_id starts with 'sh' :\n",df.loc[filt,['id','black_id']])