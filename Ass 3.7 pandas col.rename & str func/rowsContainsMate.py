import pandas as pd
df=pd.read_csv('games.csv')
filt = df['victory_status']=='mate'
print("All The rows whose victory_status is 'mate' :\n",df.loc[filt,['id','victory_status']])