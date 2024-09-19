import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])     # 创建数组a
b = np.mat(a)               # 矩阵b
c = np.mat('123;456;789')   # 矩阵c
print('创建矩阵b：\n',b)  # 打印矩阵b
print('创建矩阵c：\n',c)  # 打印矩阵c
print('矩阵b类型：',type(b),'矩阵c类型：',type(c))
print('矩阵b转为数组：',type(np.asarray(b)))    # 打印将b矩阵转换为数组类型
print('数组a转换为矩阵',type(np.asmatrix(a)))   # 打印将数组a转换为矩阵类型
