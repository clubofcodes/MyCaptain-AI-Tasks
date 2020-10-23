# import numpy as np

# arr = np.array([1,'a','b',2,'c',3,'data',5])

# print(np.sort(arr))

#1(test)
# df.drop(index=df[df['email']=='rjagetiya780@rku.ac.in'].index,axis=0,inplace=True) //go in 3.9 folder 1st.

#2

# import pandas as pd

# df=pd.read_csv('eth.csv')

# filt=(df['date']<='2018') & (df['date']>'2019')

# df.loc[filt,['Close']].mean()



#3
from matplotlib import pyplot as plt
plt.style.use('fivethirtyeight')

slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']

explode = [0,0,0,0.1,0]

plt.pie(slices, labels = labels, explode = explode, wedgeprops = {'edgecolor':'black'})

plt.title('My pie chart')
plt.show()

#4

import matplotlib.pyplot as plt
plt.plot([1,2,3],[4,5,1])
plt.show()