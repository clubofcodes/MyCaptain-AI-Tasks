import pandas,collections
from matplotlib import pyplot as plt
plt.style.use('dark_background') 

df = pandas.read_csv('data.csv')
langC = collections.Counter()
[langC.update(counts.split(';')) for counts in df['LanguagesWorkedWith']]
langs,rep_count =[],[]
[[langs.append(data[0]), rep_count.append(data[1])] for data in langC.most_common(len(langC))]

langs.reverse()
rep_count.reverse()
plt.barh(langs,rep_count, color='red')
plt.title('First 15 languages')
plt.legend(["Languages vs It's Repeat"],loc=4)
plt.xlabel('Languages Count')
plt.ylabel('Programming Languages')
plt.show()