import pandas,collections
from matplotlib import pyplot as plt
plt.style.use('dark_background') 

df = pandas.read_csv('data.csv')
langC = collections.Counter()
[langC.update(counts.split(';')) for counts in df['LanguagesWorkedWith']]
langs,rep_count =[],[]
[[langs.append(data[0]), rep_count.append(data[1])] for data in langC.most_common(15)]

plt.plot(rep_count,langs,marker='.') 
plt.tight_layout()
plt.title('First 15 languages')
plt.legend(["Languages vs It's Repeat"])
plt.xlabel('Languages Count')
plt.ylabel('Programming Languages')
plt.show()