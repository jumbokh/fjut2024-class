
#对指标进行去量纲化处理
import pandas as  pd
import numpy as np
pd.set_option('display.float_format', lambda x: '%.3f' % x)
data = pd.read_csv('中小微企业信贷决策/数据集/指标数据集.csv',encoding='utf-8-sig',engine="python")
data1 = data[['企业代号','企业规模','经营成果','议价能力','企业长期盈利变化']]#为后续存储最终得分准备框架
data = data[['企业规模','经营成果','议价能力','企业长期盈利变化']]#从数据指标集当中选取建立矩阵所需的四个指标：企业规模、经营成果、议价能力、企业长期盈利变化
data = (data - np.min(data,axis=0)) / (np.max(data,axis=0) - np.min(data,axis=0))

#计算概率矩阵
sumzb = np.sum(data, axis=0)
data_1 = data / sumzb
a = data_1*1.0
#计算每个指标的信息熵
n, m = np.shape(data_1)
epsilon = 1e-5
e=(-1.0/np.log(n+epsilon))*np.sum(data_1*np.log(a+epsilon),axis=0)
#计算效用值1-e，归一化得到权重
w=(1-e)/np.sum(1-e)
print(w)
#计算每家公司最终得分 
recodes=np.sum(data*w*100,axis=1)
data1['最终得分']= recodes
print(data1)
data1.to_csv('中小微企业信贷决策/企业最终得分.csv',encoding = 'utf-8-sig',index = None )