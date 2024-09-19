import numpy as np                # 导入numpy模块

a = np.logspace(0,9,10)            # 创建数值10的0~9幂，数组长度为10
print('数值10的0~9幂')
print('数组内容为： \n',a)         # 打印数组内容
print('数组长度为：',a.size)       # 打印数组长度
print('-------------------')
b = np.logspace(0,9,10,base=2)     # 创建数值2的0~9幂，数组长度为10
print('数值2的0~9幂')
print('数组内容为： \n',b)         # 打印数组内容
print('数组长度为：',b.size)       # 打印数组长度