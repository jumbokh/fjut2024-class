import pandas as pd

df = pd.read_csv('信用卡欺诈检测/数据结果/删除重复数据.csv',engine="python")
print(df.head())

df = df.dropna()
print(df.head())

df.to_csv('信用卡欺诈检测/数据结果/数据清洗结果.csv', index=False, encoding='utf-8-sig')

