import numpy as np  # 导入函数模块
import matplotlib.pyplot as plt  # 导入绘图模块
import matplotlib  # 导入图表模块

# 避免中文乱码
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False
a = 2   # 数据a
# 随机生成数据a的坐标点
x = np.random.randn(a)
y = np.random.randn(a)
b = 20  # 数据b
# 随机生成数据b的坐标点
x_b = np.random.randn(b)
y_b = np.random.randn(b)

plt.scatter(x, y,c='r',marker='>')   # 绘制数据a的散点图
plt.scatter(x_b, y_b,c='b',marker='o')   # 绘制数据b的散点图
plt.legend(['数据a','数据b'])            # 添加图例
plt.show()                               # 显示散点图
