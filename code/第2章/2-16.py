import numpy as np                # 导入numpy模块

a = np.array([[1,2],[3,4]])        # 创建数组a
print('数组a为：\n',a)             # 打印数组a
b = np.array([[5,6],[7,8]])        # 创建数组b
print('数组b为：\n',b)             # 打印数组b
c = np.concatenate((a,b))          # 默认组合
print('默认组合的数组为：\n',c)    # 打印默认组合的数组
d = np.concatenate((a,b),axis=1)   # 将对应行的数组进行组合
print('组合对应行的数组为：\n',d)  # 打印组合对应行的数组
e = np.concatenate((a,b,[[9,0],[0,9]]),axis=1)  # 组合多个数组
print('组合多个数组为：\n',e)      # 打印组合多个数组
