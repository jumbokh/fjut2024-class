import numpy as np                # 导入numpy模块

a = np.arange(9).reshape(3,3)   # 创建形状3*3的数组
b = np.hsplit(a,3)              # 根据形状分割为3个子数组
print('原数组为：\n',a)         # 打印原数组
print('分割后的数组：\n',b)     # 打印分割后的3个数组
