import pandas as pd
df=pd.read_csv('games.csv')
print(df.columns)
df=df.rename(columns={'moves':'game moves','opening_ply':'opening_play'})
print(df.columns)
print("After Changing the name of 'moves' column to 'game moves' .and 'opening_ply' column to 'opening_play' :\n",df.loc[:,['game moves','opening_play']])