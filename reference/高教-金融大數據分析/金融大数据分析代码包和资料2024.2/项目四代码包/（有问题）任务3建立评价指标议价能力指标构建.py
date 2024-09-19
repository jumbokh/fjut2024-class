#导入pandas及numpy库
import pandas as pd
import numpy as np
pd.set_option('display.float_format', lambda x: '%.3f' % x)
#读取数据集并进行处理
df1 = pd.read_csv('中小微企业信贷决策/数据集/销项发票.csv',encoding='utf-8-sig',engine="python")
df2 = pd.read_csv('中小微企业信贷决策/数据集/进项发票.csv',encoding='utf-8-sig',engine="python")
df1 = df1[df1['发票状态'].isin(['有效发票'])]
df2 = df2[df2['发票状态'].isin(['有效发票'])]
#计算上下游商户数量
df1 = df1.groupby('企业代号')['购方单位代号'].nunique() #以企业代号为分组，对下游客户进行汇总
df2 = df2.groupby('企业代号')['销方单位代号'].nunique() #以企业代号为分组，对上游商户进行汇总
table = pd.merge(df1, df2, left_index=True, right_index=True)
table['议价能力'] = table['销方单位代号'] + table['购方单位代号']#计算上下游商户总和
print(table)
table.to_csv('中小微企业信贷决策/议价能力.csv',encoding = 'utf-8-sig')