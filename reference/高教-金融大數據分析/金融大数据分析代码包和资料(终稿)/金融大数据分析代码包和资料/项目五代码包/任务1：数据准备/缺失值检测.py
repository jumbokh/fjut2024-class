import pandas as pd 

df = pd.read_csv('信用卡欺诈检测/数据来源/信用卡数据.csv',engine="python",encoding="utf-8")
print(df.head)
print(df.isnull().any(axis=0))
print(df.isnull().values.sum())



