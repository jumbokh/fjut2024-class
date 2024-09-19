import numpy as np                # 导入函数模块
import matplotlib                  # 导入图表模块
import matplotlib.pyplot as plt   # 导入绘图模块

# 避免中文乱码
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False
x = np.arange(1, 50)                 # 绘制数据0-50
fig, axes = plt.subplots(2, 2)       # 创建4个子图，2行2列
x1 = axes[0, 0]                      # 子图1位置
x2 = axes[0, 1]                      # 子图2位置
x3 = axes[1, 0]                      # 子图3位置
x4 = axes[1, 1]                      # 子图4位置
x1.plot(x, x)                        # 绘制子图1
x2.plot(x, -x)                       # 绘制子图2
x3.plot(x, x ** 2)                   # 绘制子图3
x4.plot(x, np.log(x))                # 绘制子图4
plt.show()                           # 显示图表
