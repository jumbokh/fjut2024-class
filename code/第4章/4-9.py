from mpl_toolkits.mplot3d import Axes3D    # 绘制3D坐标的函数
import matplotlib.pyplot as plt              # 绘图用的模块
import numpy as np                              # 导入函数模块
import matplotlib                               # 导入图表模块
# 避免中文乱码
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False
fig = plt.figure()                          # 创建图形画布
ax = Axes3D(fig)                            # 创建3D图形画布
colors = ['r', 'g', 'b']                    # 定义颜色列表
year  =  [2016, 2017, 2018]                 # 定义年份列表
for z,color in zip(year,colors):           # 循环遍历坐标数据
    x = range(1, 13)                        # 月份数据
    y = 100000 * np.random.rand(12)         # 模拟销量数据
    # 绘制条形图，zdir参数为将y轴数据与z轴调换位置
    ax.bar(x, y, zs=z, zdir='y', color=color, alpha=0.8)  
ax.set_xlabel('月份')
ax.set_ylabel('年份')
ax.set_zlabel('销量')
ax.set_yticks(year)                          # y轴只显示年份数据
plt.show()                                   # 显示图表
