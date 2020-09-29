import pandas as pd

sr = pd.Series(['Hellish','RJ',7,5])
print("Default Series :\n",sr,"\n")
print("Series using map() method :\n",sr.map('I am a {}'.format))