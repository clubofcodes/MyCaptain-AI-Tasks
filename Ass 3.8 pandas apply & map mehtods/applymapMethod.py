import pandas as pd

df = pd.DataFrame([[9,25],[8,24],[7,23]],columns=['R','J'])
print("Default Dataframe :\n",df,"\n")
print("SquareRoot using applymap() method :\n",df.applymap(lambda x: x**(1/2)))
