import pandas as pd

df = pd.DataFrame([[9,25],[8,24],[7,23]],columns=['R','J'])
print("Default Dataframe :\n",df,"\n")
print("Dataframe using replace() method :\n",df.replace({'R':{9:81,7:49},'J':{25:2}}))