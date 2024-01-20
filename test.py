import pandas as pd


Data=[
    {"name":"Riad","age":25,"city":"chittagong"},
    {"name":"Ripon","age":25,"city":"chittagong"},
    {"name":"Nishad","age":27,"city":"Dhaka"},
    {"name":"Faisal","age":25,"city":"chittagong"},

]


Data=pd.DataFrame(Data)
Data.to_csv("Data/data.csv",index=False)