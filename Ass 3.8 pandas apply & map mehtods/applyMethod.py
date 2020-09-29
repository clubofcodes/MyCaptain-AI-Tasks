import pandas as pd
import numpy as np

df = pd.DataFrame([[9,25],[8,24],[7,23]],columns=['R','J'])
print("Default Dataframe :\n",df,"\n")
print("SquareRoot using apply() method :\n",df.apply(np.sqrt))
