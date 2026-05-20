import pandas as pd
s = pd.read_csv("data.csv")
print(s.isnull().sum())