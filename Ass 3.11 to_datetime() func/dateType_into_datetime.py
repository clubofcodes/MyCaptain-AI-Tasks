import pandas as pd
df = pd.read_csv("ETH.csv") #cd ..
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d %I-%p')
print("The Converted type of column 'Date' is :\n",df['Date'].head(1))