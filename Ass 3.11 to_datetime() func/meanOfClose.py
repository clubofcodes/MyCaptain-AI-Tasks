import pandas as pd
df = pd.read_csv("ETH.csv") #cd ..
filt = df['Date'].str.contains('2018')
print("The mean of column 'Close' for the year 2018 is :",df.loc[filt,'Close'].mean().round(2))