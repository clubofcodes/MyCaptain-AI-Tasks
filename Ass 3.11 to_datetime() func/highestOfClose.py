import pandas as pd
df = pd.read_csv("ETH.csv") #cd ..
filt1 = df['Date'].str.contains('2019')
filt2 = df['Date'].str.contains('2020')
print("The highest value of column 'Open' for the year 2019 is :",df.loc[filt1,'Open'].max())
print("The highest value of column 'Open' for the year 2020 is :",df.loc[filt2,'Open'].max())