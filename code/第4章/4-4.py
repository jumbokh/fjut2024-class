
# 图形画布
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib  # 导入图表模块
import matplotlib.pyplot as plt # 导入绘图模块


class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None, width=0, height=0, dpi=100):
        # 避免中文乱码
        matplotlib.rcParams['font.sans-serif'] = ['SimHei']
        matplotlib.rcParams['axes.unicode_minus'] = False

    # 显示评价饼图
    def pie_chart(self, good_size, general_poor_size, title):
        """
        绘制饼图
        explode：设置各部分突出
        label:设置各部分标签
        labeldistance:设置标签文本距圆心位置，1.1表示1.1倍半径
        autopct：设置圆里面文本
        shadow：设置是否有阴影
        startangle：起始角度，默认从0开始逆时针转
        pctdistance：设置圆内文本距圆心距离
        返回值
        l_text：圆内部文本，matplotlib.text.Text object
        p_text：圆外部文本
        """
        label_list = ['好评', '中差评']  # 各部分标签
        size = [good_size, general_poor_size]  # 各部分大小
        color = ['lightblue', 'red']  # 各部分颜色
        explode = [0.05, 0]  # 各部分突出值
        plt.pie(size, colors=color, labels=label_list, explode=explode, labeldistance=1.1,
                autopct="%1.1f%%", shadow=True, startangle=0, pctdistance=0.6)
        plt.axis("equal")  # 设置横轴和纵轴大小相等，这样饼才是圆的
        plt.title(title, fontsize=12)
        plt.legend()  # 显示图例
        plt.show()    # 显示饼图

p = PlotCanvas()  # 创建画布对象
p.pie_chart(99,1,'第1名：  Python编程 从入门到实践 ')  # 调用绘制饼图的方法