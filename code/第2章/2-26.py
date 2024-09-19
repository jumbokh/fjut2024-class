import numpy as np  # 导入numpy模块

a = np.array([1,5,10])  # 一维数组a
b = np.array([[1, 3, 5], [2, 4, 6]])  # 多维数组b

print('数组a百分位为50的值：',np.percentile(a,50))    # 打印数组a百分位为50的值
print('数组b百分位为50的值：',np.percentile(b,50))    # 打印数组b百分位为50的值
# 打印以列方式计算数组b百分位为50的值
print('以列方式计算数组b百分位为50的值：',np.percentile(b,50,axis=0))
# 打印以行方式计算数组b百分位为50的值
print('以行方式计算数组b百分位为50的值：',np.percentile(b,50,axis=1))