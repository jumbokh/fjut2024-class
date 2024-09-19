import numpy as np                # 导入numpy模块

a = np.arange(9).reshape(3,3)        # 创建二维数组
print('创建的二维数组：\n',a)        # 打印创建的二维数组
print('按行展平后的数组：',a.ravel())# 打印按行展平后的数组
print('按列展平后的数组：',a.ravel(order = 'F'))  # 打印按列展平后的数组
