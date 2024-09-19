import numpy as np  # 导入numpy模块

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])  # 一维数组a
b = np.array([[1, 3, 5], [2, 4, 6], [8, 10, 12]])  # 多维数组b
print('数组a所有元素的和：', np.sum(a))  # 打印数组a所有元素的和
print('数组b所有元素的和：', np.sum(b))  # 打印数组b所有元素的和
# 打印以列方式获取数组b所有元素和
print('以列方式计算数组b所有元素和：', np.sum(b, axis=0))  
# 打印以行方式获取数组b所有元素和
print('以行方式获取数组b所有元素和：', np.sum(b, axis=1))  
