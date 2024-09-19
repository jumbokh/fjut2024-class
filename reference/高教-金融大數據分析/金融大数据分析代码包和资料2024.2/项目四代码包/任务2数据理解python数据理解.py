import pandas as pd
import numpy as np
df1 = pd.read_csv('中小微企业信贷决策/数据集/进项发票.csv',encoding = 'utf-8-sig',engine="python")
df2 = pd.read_csv('中小微企业信贷决策/数据集/销项发票.csv',encoding = 'utf-8-sig',engine="python")
print(df1.info())
print('-' * 50)
print(df2.info())
