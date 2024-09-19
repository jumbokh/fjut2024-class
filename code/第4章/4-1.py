# 图形画布
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib  # 导入图表模块
import matplotlib.pyplot as plt  # 导入绘图模块


class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None, width=0, height=0, dpi=100):
        # 避免中文乱码
        matplotlib.rcParams['font.sans-serif'] = ['SimHei']
        matplotlib.rcParams['axes.unicode_minus'] = False

    # 显示出版社占有比例的条形图
    def bar(self, number, press, title):
        """
        绘制水平条形图方法barh
        参数一：y轴
        参数二：x轴
        """
        # 设置图表跨行跨列
        plt.subplot2grid((12, 12), (1, 2), colspan=12, rowspan=10)
        # 从下往上画水平条形图
        plt.barh(range(len(number)), number, height=0.3, color='r', alpha=0.8)
        plt.yticks(range(len(number)), press)  # Y轴出版社名称显示
        plt.xlim(0, 100)  # X轴的数量0~100
        plt.xlabel("比例")  # 比例文字
        plt.title(title)  # 表标题文字
        # 显示百分比数量
        for x, y in enumerate(number):
            plt.text(y + 0.1, x, '%s' % y + '%', va='center')
        plt.show()  # 显示图表


number = [9, 2, 44, 1, 1, 5, 11, 4, 23]  # 比例数据
# 出版社数据
press = ['中国水利水电', '中国电力', '人民邮电', '北京大学', '华中科技大学', '吉林大学', '机械工业', '清华大学', '电子工业']
p = PlotCanvas()  # 创建自定义画布对象
p.bar(number, press, "前100名出版社占有比例")  # 调用显示条形图表的方法
