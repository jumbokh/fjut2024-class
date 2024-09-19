import numpy as np                # 导入numpy模块

a = np.random.uniform(range(1,6),6) # 产生5个6以内的随机小数
b = np.random.uniform(range(1,6),6) # 产生5个6以内的随机小数
print('随机产生数组a',a)
print('随机产生数组b',b)
print('数组相加结果：',np.add(a,b))
print('数组相减结果：',np.subtract(a,b))
print('数组相乘结果：',np.multiply(a,b))
print('数组相除结果：',np.divide(a,b))
print('数组a倒数结果：',np.reciprocal(a))
print('数组a对应负数为：',np.negative(a))
print('数组a对应数组b元素中的幂：',np.power(a,b))
print('数组a与数组b元素求余：',np.mod(a,b))