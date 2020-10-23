import pandas as pd
df = pd.read_csv("ETH.csv") #cd ..
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d %I-%p')
filt=df['Date']=='2020-02-21'
day=df.loc[filt,'Date'].dt.day_name()
print("The day of the date 2020-02-21 is : ",day.to_string(index=False))