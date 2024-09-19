import numpy as np                # 导入函数模块
import matplotlib                  # 导入图表模块
import matplotlib.pyplot as plt   # 导入绘图模块

# 避免中文乱码
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

x = np.arange(0,50)                # 绘制数据0-50
fig = plt.figure(figsize=(6,4))   # 设置图形画布大小
x1 = fig.add_subplot(211)          # 添加子图x1，211代表2行1列第1个位置
plt.title('子图x1')                # 设置标题子图x1
x1.plot(x, x)                      # 绘制线图
x2 = fig.add_subplot(212)          # 添加子图x2，212代表2行1列第2个位置
plt.title('子图x2')                # 设置标题子图x2
x2.plot(x, x ** 2)                 # 绘制线图
plt.show()                         # 显示图表
