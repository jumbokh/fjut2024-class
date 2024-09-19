import numpy as np                # 导入numpy模块

a = np.array([[1,2],[3,4]])        # 创建数组a
print('数组a为：\n',a)             # 打印数组a
b = np.array([[5,6],[7,8]])        # 创建数组b
print('数组b为：\n',b)             # 打印数组b
c = np.hstack((a,b))               # 横向组合数组
d = np.vstack((a,b))               # 纵向组合数组
print('横向组合后的数组为：\n',c)    # 打印横向组合后的数组
print('纵向组合后的数组为：\n',d)    # 打印纵向组合后的数组
