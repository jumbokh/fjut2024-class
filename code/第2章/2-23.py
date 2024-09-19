import numpy as np  # 导入numpy模块

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])  # 一维数组a
b = np.array([[1, 3, 5], [2, 4, 6], [8, 10, 12]])  # 多维数组b
print('数组a中最大元素为：', np.amax(a))  # 打印数组a中最大元素
print('数组b中最大元素为：', np.amax(b))  # 打印数组b中最大元素
print('原数组b：\n', b)  # 打印原数组b
print('以列方式获取数组b最大元素为：', np.amax(b, axis=0))  # 打印以列方式获取数组b最大元素
print('以行方式获取数组b最大元素为：', np.amax(b, axis=1))  # 打印以行方式获取数组b最大元素

