#for practice and diff logic.
# import pandas as pd
# df = pd.read_csv("ETH.csv") #cd ..
# filt = df['Date'].str.contains('2020-01')
# df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d %I-%p')
# df['Day'] = df['Date'].dt.day_name()
# days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
# print('Day wise max value of High column of January - 2020 are :\n')
# for day in days:
#     grouped = df.groupby('Day').get_group(day)
#     print(day," : ",grouped.loc[filt,'High'].max())

#real code
import pandas as pd
d_parser=lambda x: pd.datetime.strptime(x,'%Y-%m-%d %I-%p')
df=pd.read_csv('ETH.csv',parse_dates=['Date'],date_parser=d_parser)
df['Day'] = df['Date'].dt.day_name()
df.set_index('Date', inplace=True)
print('Day wise max value of High column of January - 2020 are :\n',df.loc['2020-01'][{'High':'High','Day':'Day'}].resample('D').max())