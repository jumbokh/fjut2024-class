import numpy as np  # 导入numpy模块

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])  # 一维数组a
b = np.array([[1, 3, 5], [2, 4, 6], [8, 10, 12]])  # 多维数组b
print('数组a中元素差为：', np.ptp(a))  # 打印数组a中元素差
print('数组b中元素差为：', np.ptp(b))  # 打印数组b中元素差
print('以列方式计算数组b元素差为：', np.ptp(b, axis=0))  # 打印以列方式计算数组b的元素差
print('以行方式计算数组b元素差为：', np.ptp(b, axis=1))  # 打印以行方式计算数组b的元素差
