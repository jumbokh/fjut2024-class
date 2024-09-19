#导入pandas及numpy库
import pandas as pd
import numpy as np
pd.set_option('display.float_format', lambda x: '%.3f' % x)

#建立“企业规模”指标
df =pd.read_csv('中小微企业信贷决策/数据集/销项发票.csv',encoding = 'utf-8-sig',engine="python")#在*号处填写读取原始数据表格代码

#筛选出有效发票
df1 = df[df['发票状态'].isin(['有效发票'])]  #在引号里填写需要筛选出的内容

#以企业代号为分组单位，将销项发票金额进行汇总
#在index括号当中填写分组情况，在values括号当中填写需要汇总的金额指标
df2 = pd.pivot_table(df1, index=[u'企业代号'], values=[u'金额'], aggfunc=[np.sum])
#显示结果并导出文件
print(df2)
df2.to_csv('中小微企业信贷决策/企业规模.csv',encoding = 'utf-8-sig')
