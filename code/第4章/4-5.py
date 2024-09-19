import matplotlib  # 导入图表模块
import matplotlib.pyplot as plt  # 导入绘图模块

# 避免中文乱码
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

data = [[100,500,300,400,800],[80,150,340,210,500]]  # 模拟工厂A与工厂B的年产值数据
labels = ['工厂A', '工厂B']  # 工厂名称
plt.boxplot(data,labels=labels) # 绘制箱形图
plt.title('2018（工厂A）与（工厂B）年产值箱形图')  # 标题
plt.show()  # 显示箱形图
