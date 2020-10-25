import pandas as pd
d_parser=lambda x: pd.datetime.strptime(x,'%Y-%m-%d %I-%p')
df=pd.read_csv('ETH.csv',parse_dates=['Date'],date_parser=d_parser) #cd ..
df.set_index('Date',inplace=True)
print('Day wise values of are :\n',df.resample('D').agg({'High':'min','Open':'max','Close':'mean'}).round(2))