import numpy as np                # 导入numpy模块

a = np.zeros(4)                    # 默认为浮点类型
print('数组a内容为：',a)            # 打印数组内容
print('数组a类型为：',a.dtype)      # 打印数组类型
print('数组a形状为：',a.shape)      # 打印数组形状
print('数组a维数为：',a.ndim)       # 打印数组维数
print('---------------------')
b = np.zeros(4, dtype=np.int)      # 设置类型为整数
print('数组b内容为：',b)            # 打印数组内容
print('数组b类型为：',b.dtype)      # 打印数组类型
print('---------------------')
c = np.zeros((3,3))                 # 生成3*3二维数组
print('数组c内容为：\n',c)          # 打印数组内容
print('数组c形状为：',c.shape)      # 打印数组形状
print('数组c维数为：',c.ndim)       # 打印数组维数