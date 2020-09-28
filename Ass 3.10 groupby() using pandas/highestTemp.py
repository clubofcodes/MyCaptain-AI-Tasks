import pandas as pd
df = pd.read_csv("forestfires.csv")
val,key = [],[]
[key.append(i) for i in df.groupby('month').groups]
[val.append(i) for i in df.groupby('month')['temp'].agg(max)]
print("Below data shows highest temperature of every month :\n",pd.DataFrame({'Month':key,'Temp':val}))