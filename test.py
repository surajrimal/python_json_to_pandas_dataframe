import pandas as pd
import json 

with open('yourfile.json') as json_file:
    data = json.load(json_file)

df= pd.json_normalize(data,max_level=1)
#max_level is for nested json
print(df)
