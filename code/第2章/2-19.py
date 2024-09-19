import numpy as np                # 导入numpy模块

a = np.arange(9)                # 创建数组
b = np.split(a,3)               # 平均分割3个数组
c = np.split(a,[2,4,6])         # 数组分割
print('原数组为：',a)           # 打印原数组
print('平均分割后的数组：',b)   # 打印平均分割后的数组
print('数组分割后的数组：',c)   # 打印数组分割后的数组
