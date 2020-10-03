import pandas as pd
stud = {
    'name': ['RJ', 'DJ', 'DS'], 
    'en_no.': ['18SOEIT11009', '19SOEIT13001', '18SOEIT11006'], 
    'email': ['rjagetiya780@rku.ac.in', 'dj3750@rku.ac.in', 'dshukla780@rku.ac.in'],
}
df = pd.DataFrame(stud)
print("Default Dataframe :\n",df)

df.sort_values('name',inplace=True)
print("Sorting by values acc to name-wise :\n",df)

df.set_index('en_no.',inplace=True)
df.sort_index(ascending=True, inplace=True)
print("Sort by columns acc to en_no.wise :\n",df)