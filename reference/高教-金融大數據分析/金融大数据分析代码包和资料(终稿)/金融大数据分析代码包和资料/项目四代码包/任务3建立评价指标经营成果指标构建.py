#导入pandas及numpy库
import pandas as pd
import numpy as np
pd.set_option('display.float_format',lambda x : '%.3f' % x)
df = pd.read_csv('中小微企业信贷决策/数据集/进项发票.csv',encoding = 'utf-8-sig',engine="python")#读取原始数据表格，在*号处填写编码类型为utf-8-sig
#筛选出有效发票
df1= df[df["发票状态"].isin(['有效发票'])]
#以企业代号为分组单位，将进项发票金额进行汇总
df2= pd.pivot_table(df1, index=[u'企业代号'], values=[u'金额'], aggfunc=[np.sum])
#显示结果并导出文件
print(df2)
#导入上一步骤构建“企业规模”指标代码，获取销售总额
df3 = pd.read_csv('中小微企业信贷决策/数据集/销项发票.csv',encoding='utf-8-sig',engine="python")
df4= df3[df3['发票状态'].isin(['有效发票'])]
df5 = pd.pivot_table(df4, index=[u'企业代号'], values=[u'金额'], aggfunc=[np.sum])
#以企业代号作为索引将两张表进行链接
table = df5.merge(df2,on='企业代号')   #补充df5和df2进行表格关联代码，在on= 内*号内容填写关联索引
print(table)
#求出销售收入与采购成本的差值，行程经营成果指标
table['差值'] = table['sum_x'] - table['sum_y']
#显示结果并导出文件
print(table)
table.to_csv('中小微企业信贷决策/经营成果.csv',encoding = 'utf-8-sig')