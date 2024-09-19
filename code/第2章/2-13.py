import numpy as np                # 导入numpy模块

a = np.arange(9)                   # 创建数组
print('原始数组为：',a)            # 打印原始数组
b = a.reshape(3,3)                 # 修改数组形状
print('修改后的数组为：\n',b)      # 打印修改后的数组
print('修改后数组维度：',b.ndim)   # 打印修改后数组的维度
