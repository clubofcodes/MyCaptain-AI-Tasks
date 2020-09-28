import pandas as pd
import numpy as np
df = pd.read_csv("forestfires.csv")
key,median,mean,minimum,maximum = [],[],[],[],[]
[key.append(i) for i in df.groupby('month').groups]
[median.append(i) for i in df.groupby('month')['FFMC'].median()]
[mean.append(i) for i in df.groupby('month')['FFMC'].mean()]
[minimum.append(i) for i in df.groupby('month')['FFMC'].min()]
[maximum.append(i) for i in df.groupby('month')['FFMC'].max()]
print("Below data shows median, mean, min, max of column FFMC month wise :\n",pd.DataFrame({'Month':key,'FFMC(median)':median,'FFMC(mean)':mean,'FFMC(min)':minimum,'FFMC(max)':maximum}))