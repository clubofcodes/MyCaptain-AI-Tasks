import pandas as pd
d_parser=lambda x: pd.datetime.strptime(x,'%Y-%m-%d %I-%p')
df = pd.read_csv("ETH.csv",parse_dates=['Date'],date_parser=d_parser) #cd ..
df.set_index('Date',inplace=True)
print("The week wise average value of Close column of Dataframe:\n",df[{'Close':'Close'}].resample('W').mean())
