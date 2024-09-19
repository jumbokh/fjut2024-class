import numpy as np                # 导入numpy模块

a = np.random.randint(2,10, size=(2,2,3))          # 创建随机数组
print('数组内容为： \n',a)                         # 打印数组内容
print('数组形状为：',a.shape)                       # 打印数组形状

