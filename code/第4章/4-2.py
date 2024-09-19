# 图形画布
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib  # 导入图表模块
import matplotlib.pyplot as plt # 导入绘图模块


class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None, width=0, height=0, dpi=100):
        # 避免中文乱码
        matplotlib.rcParams['font.sans-serif'] = ['SimHei']
        matplotlib.rcParams['axes.unicode_minus'] = False


    # 显示前十名价格趋势的折线图
    def broken_line(self, y):
        '''
        y:y轴折线点，也就是价格
        linewidth:折线的宽度
        color：折线的颜色
        marker：折点的形状
        markerfacecolor：折点实心颜色
        markersize：折点大小
        '''
        x = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']  # X轴折线点，也就是排名
        plt.plot(x, y, linewidth=3, color='r', marker='o',
                 markerfacecolor='blue', markersize=8)  # 绘制折线，并在折点添加蓝色圆点
        plt.xlabel('排名')
        plt.ylabel('价格')
        plt.title('前10名价格走势图')  # 标题名称
        plt.grid()  # 显示网格
        plt.show()  # 显示折线图
y = [71.0, 94.1, 47.1, 72.4, 86.1, 79.0, 71.0, 73.3, 55.0, 39.1]   # y轴价格数据
p = PlotCanvas()  # 创建画布对象
p.broken_line(y)  # 调用绘制折线图的方法
