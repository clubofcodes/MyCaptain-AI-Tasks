import pandas,collections

df = pandas.read_csv('data.csv')
langC = collections.Counter()
[langC.update(counts.split(';')) for counts in df['LanguagesWorkedWith']]
langs,rep_count =[],[]
[[langs.append(data[0]), rep_count.append(data[1])] for data in langC.most_common(len(langC))]
print("The information such as languages and their count:\n",pandas.DataFrame({'Language':langs,'Count':rep_count}))