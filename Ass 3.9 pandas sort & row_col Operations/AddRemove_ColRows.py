import pandas as pd
stud = {
    'name': ['RJ', 'DJ', 'DS'], 
    'en_no.': ['18SOEIT11009', '19SOEIT13001', '18SOEIT11006'], 
    'email': ['rjagetiya780@rku.ac.in', 'dj3750@rku.ac.in', 'dshukla780@rku.ac.in']
}
df = pd.DataFrame(stud)
print("Default Dataframe :\n",df)

df['year'] = [2022,2022,2022]
print("After adding year column :\n",df)

df = df.append({'name':'VJ','year':2022}, ignore_index=True)
print("After adding row in Dataframe :\n",df) 

df.drop(columns=['email'], inplace=True)
print("After removing email column :\n",df) 

df.drop(index=3, inplace=True)
print("After removing VJ row data :\n",df)