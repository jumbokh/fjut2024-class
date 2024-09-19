

#导入操作所需相关Python库
import pandas as pd
import numpy as np
from datetime import datetime
import time
pd.set_option('display.float_format', lambda x: '%.3f' % x)
#读取数据
df = pd.read_csv('中小微企业信贷决策/数据集/销项发票.csv',encoding='utf-8-sig',engine="python")
df1 = df[df['发票状态'].isin(['有效发票'])]
#将日期转换为datetime格式
time_data = pd.to_datetime(df1["开票日期"],format='%Y/%m/%d')
df2=df1.copy()
df2['开票日期'] = time_data#建立新dataframe，将转换格式后的日期替换原数值
# 获取年
df2["year"] = pd.DatetimeIndex(df2['开票日期']).year
# 获取月份
df2["month"] = pd.DatetimeIndex(df2['开票日期']).month
#以企业、年、月作为索引建立透视表
df2 = pd.pivot_table(df2, index=[u'企业代号', u'year',u'month'], values=[u'金额'], aggfunc=[np.sum])#在index内部填写需要建立透视索引的变量：企业、年、月
df2.to_csv('中小微企业信贷决策/月度利润.csv')
#导入微调数据集，建立辅助指标date
df3= pd.read_csv('中小微企业信贷决策/数据集/月度利润_1.csv',encoding='utf-8-sig',engine="python")
df3 = df3.astype(str)
df3['date'] = df3['year'] + df3['month']
#建立映射，调整辅助索引
size_mapping = {'20171':1,'20172':2,'20173':3,'20174':4,'20175':5,'20176':6,
'20177':7,'20178':8,'20179':9,'201710':10,'201711':11,'201712':12,'20181':13,
'20182':14,'20183':15,'20184':16,'20185':17,'20186':18,'20187':19,'20188':20,
'20189':21,'201810':22,'201811':23,'201812':24,'20191':25,'20192':26,'20193':27,
'20194':28,'20195':29,'20196':30,'20197':31,'20198':32,'20199':33,'201910':34,'201911':35,'201912':36}
df3['date'] = df3['date'].map(size_mapping)

#调整数据格式，建立辅助指标,形成辅助指标数据集
df3['金额'] = df3['金额'].astype('float')
df3['x*y'] =  df3['date'].mul(df3['金额'])
df3['x^2'] =  df3['date'].mul(df3['date'])
df3['x'] = df3['date']
df3['y'] = df3['金额']
#建立透视表，在汇总结果*号处填写平均值和汇总加和数据
df3_1 = pd.pivot_table(df3, index=[u'企业代号'], values=[u'x*y',u'x^2',u'x',u'y'], aggfunc=[np.sum,np.mean])
df3_1.to_csv('中小微企业信贷决策/res.csv')
#读取res微调后数据集
df3_2 = pd.read_csv('中小微企业信贷决策/数据集/res_1.csv',encoding='utf-8-sig',engine="python")
#构建函数，建立“企业长期盈利变化”指标'k'
df3_2['k'] = (df3_2['x*y']-df3_2['x']*df3_2['y'])/(df3_2['y_sum']*(df3_2['x^2']-df3_2['x']*df3_2['x']))
df3_2.to_csv('中小微企业信贷决策/企业长期盈利变化.csv',encoding = 'utf-8-sig')
print(df3_2)