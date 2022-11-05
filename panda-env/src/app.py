import pandas as pd
file= "./Notes.xlsx"
df = pd.read_excel(file,sheet_name="Sheet1")
print("🐼🐼🐼 FUNCTIONS IN PANDA FOR A DF(data frame) 🐼🐼🐼 ")
print("*******************************************************")
print(df.shape)
print("*******************************************************")
print(df.info())
print("*******************************************************")
print(df.size)
print("*******************************************************")
print(df.head())
print("*******************************************************")
print(df.tail())
print("*******************************************************")
print(df.describe())
print("*******************************************************")
print(df.sample(2))
print("*******************************************************")
print(df.iloc[3])
print("*******************************************************")
print(df[2:9])#range
