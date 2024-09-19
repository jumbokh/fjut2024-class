# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
import re

import urllib.request
import json
import pandas as pd


# pyecharts 、echarts_china_cities_pypkg 、
# echarts_china_provinces_pypkg 、echarts_countries_pypkg
from pyecharts import Geo,Line,Bar

from pyecharts import Overlap  # 图表叠加类


from wordcloud import WordCloud, ImageColorGenerator    # 词云图相关模块
import matplotlib.pyplot as plt                         # 绘制图表的模块
from os import path                                     # 路径
import collections                                      # 集合模块
import jieba                                            # 分词模块
import imageio                                          # 图片读取

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *

# 显示热力图，主要城市评论数_平均分页面
class MainWindows(QMainWindow):
    def __init__(self):
        super(QMainWindow,self).__init__()     # 初始化
        self.setGeometry(200, 200, 1250, 650)  # 设置窗体大小
        self.browser = QWebEngineView()        # 创建html文件显示控件
    def kk(self,title,hurl):                   # 自定义方法
        self.setWindowTitle(title)             # 设置窗体显示的标题文字
        url = d+'/'+hurl                       # 拼接文件路径
        self.browser.load(QUrl(url))           # 加载html文件
        self.setCentralWidget(self.browser)    # 设置显示html文件的控件

# 显示词云图窗体
class MainWindowy(QMainWindow):
    def __init__(self):
        super(QMainWindow,self).__init__()      # 初始化
        self.setGeometry(200, 200, 650, 650)    # 设置窗体大小
        self.browser = QLabel()                 # 创建QLabel控件用于显示词云图
    def kk(self,title,hurl):                    # 自定义方法
        self.setWindowTitle(title)              # 设置窗体显示的标题文字
        url = d+'/'+hurl                        # 拼接文件路径
        # 通过pixmap解析图片
        pixmap = QPixmap(url)
        # 设置图片
        self.browser.setPixmap(pixmap)
        # 显示控件
        self.browser.show()
        self.setCentralWidget(self.browser)      # 设置显示图片的控件

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(405, 206)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(48, 20, 311, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox.setDuplicatesEnabled(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 80, 331, 106))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_4.addWidget(self.pushButton_4)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "开心麻花影视作品分析"))
        self.label.setText(_translate("Form", "选择电影："))
        self.comboBox.setItemText(0, _translate("Form", "夏洛特烦恼"))
        self.comboBox.setItemText(1, _translate("Form", "羞羞的铁拳"))
        self.comboBox.setItemText(2, _translate("Form", "西虹市首富"))
        self.pushButton.setText(_translate("Form", "分析"))
        self.label_2.setText(_translate("Form", "主要城市评论数-及平均分："))
        self.pushButton_2.setText(_translate("Form", "查看"))
        self.label_3.setText(_translate("Form", "                 热力图："))
        self.pushButton_3.setText(_translate("Form", "查看"))
        self.label_4.setText(_translate("Form", "                   词云："))
        self.pushButton_4.setText(_translate("Form", "查看"))
        # 绑定电影选择处理方法
        self.comboBox.activated[str].connect(self.itemchange)
        # 分析按钮事件的绑定
        self.pushButton.clicked.connect(self.anal)
        # 判断是否有词云图片
        if not os.path.isfile(d +  '夏洛特烦恼词云.png'):
            self.pushButton.setText('分析')
            self.hide()
        else:
            self.pushButton.setText('完成重新分析')
            self.moveName = '夏洛特烦恼'
            self.moveId = '246082'
            self.show()
            self.btnclick()

    # 隐藏查看内容
    def hide(self):
        self.pushButton_4.setVisible(False)
        self.label_4.setVisible(False)
        self.pushButton_3.setVisible(False)
        self.label_3.setVisible(False)
        self.pushButton_2.setVisible(False)
        self.label_2.setVisible(False)
    # 显示查看内容
    def show(self):
        self.pushButton_4.setVisible(True)
        self.label_4.setVisible(True)
        self.pushButton_3.setVisible(True)
        self.label_3.setVisible(True)
        self.pushButton_2.setVisible(True)
        self.label_2.setVisible(True)
    # 下拉列表电影选择的事件
    def itemchange(self, text):
        # 判断下拉列表改变后的内容是什么
        if text == '夏洛特烦恼':
            # 判断文件是否存在
            if not os.path.isfile(d + '夏洛特烦恼词云.png'):
                # 文件不存在设置按钮显示文字‘分析’
                self.pushButton.setText('分析')
                # 隐藏查看部分部分的控件
                self.hide()
            else:
                # 文件存在设置按钮显示文字为‘完成重新分析’
                self.pushButton.setText('完成重新分析')
                # 设置名称变量内容
                self.moveName = '夏洛特烦恼'
                # 设置id变量内容
                self.moveId = '246082'
                # 显示查看部分内容
                self.show()
                # 调用自定义查看按钮绑定事件方法
                self.btnclick()
        if text == '羞羞的铁拳':
            if not os.path.isfile(d + '羞羞的铁拳词云.png'):
                self.pushButton.setText('分析')
                self.hide()
            else:
                self.pushButton.setText('完成重新分析')
                self.moveName = '羞羞的铁拳'
                self.moveId = '1198214'
                self.show()
                self.btnclick()
        if text == '西虹市首富':
            if not os.path.isfile(d + '西虹市首富词云.png'):
                self.pushButton.setText('分析')
                self.hide()
            else:
                self.pushButton.setText('完成重新分析')
                self.moveName = '西虹市首富'
                self.moveId = '1212592'
                self.show()
                self.btnclick()
    # 分析事件
    def anal(self):
        #  夏洛特烦恼 246082
        if self.comboBox.currentIndex() == 0:
            self.moveName = '夏洛特烦恼'
            self.moveId = '246082'
            self.getData()
        #  羞羞的铁拳 1198214
        if self.comboBox.currentIndex() == 1:
            self.moveName = '羞羞的铁拳'
            self.moveId = '1198214'
            self.getData()
        #  西虹市首富 1212592
        if self.comboBox.currentIndex() == 2:
            self.moveName = '西虹市首富'
            self.moveId = '1212592'
            self.getData()
        self.show()     # 显示查看部分的控件
        self.pushButton.setText('完成重新分析')
        self.btnclick()
    # 获取数据以及分析数据的方法
    def getData(self):
        # # 创建临时数据表
        # tomato = pd.DataFrame(columns=['date', 'score', 'city', 'comment', 'nick'])
        # i=1      # 初始化页码
        # while True:
        #     print('第',i,'页数据！')
        #     try:
        #         # 获取信息的网络请求地址
        #         url = 'http://m.maoyan.com/mmdb/comments/movie/'+self.moveId+'.json?_v_=yes&offset='+ str(i)
        #         # html = urllib.request.urlopen(url)          # 发送网络请求
        #         # 创建浏览器头部信息
        #         headers = ("User-Agent",
        #                    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE")
        #         opener = urllib.request.build_opener()    # 创建build_opener对象
        #         opener.addheaders = [headers]             # 添加浏览器头部信息
        #         html = opener.open(url)                   # 发送网路请求
        #         # 读取返回内容
        #         content = html.read()
        #         total = json.loads(content)['total']        # 该值为0说明没有下一页信息
        #         print(total)
        #         if i==5:
        #             break
        #         # if total == 0:
        #         #     # 结束循环
        #         #     break
        #         else:
        #             data = json.loads(content)['cmts']    # 解析第一部分数据
        #             datah = json.loads(content)['hcmts']  # 解析第二部分数据
        #             # 通过for循环将第一部分数据添加到临时的数据表中
        #             for item in data:
        #                 tomato = tomato.append(
        #                     {'date': item['time'].split(' ')[0], 'city': item['cityName'],
        #                      'score': item['score'],'comment': item['content'],
        #                      'nick': item['nick']}, ignore_index=True)
        #             for item in datah:
        #                 tomato = tomato.append(
        #                     {'date': item['time'].split(' ')[0], 'city': item['cityName'],
        #                      'score': item['score'],'comment': item['content'],
        #                      'nick': item['nick']}, ignore_index=True)
        #         i +=1
        #     except Exception as e:
        #         i += 1
        #         print(e)    # 打印异常
        #         # 跳出本次循环
        #         continue
        # # 去掉重复数据
        # tomato = tomato.drop_duplicates(subset=['date', 'score', 'city', 'comment', 'nick'], keep='first')
        # # 生成xlsx文件
        # tomato.to_excel(self.moveName+'.xlsx', sheet_name='data')



        # 读取文件内容
        tomato_com = pd.read_excel(self.moveName + '.xlsx')
        grouped = tomato_com.groupby(['city'])  # 按照城市名称进行数据的分组
        grouped_pct = grouped['score']  # 获取分组后的评分信息
        city_com = grouped_pct.agg(['mean', 'count'])  # 聚合数据，城市、平均分、数量
        # 重置数据的索引
        city_com.reset_index(inplace=True)
        # 返回浮点数 0.01 返回到后两位
        city_com['mean'] = round(city_com['mean'], 2)
        # 创建热力图实例对象
        geo = Geo('《' + self.moveName + '》 全国热力图', title_color="#fff",
                  title_pos="center", width=1200,
                  height=600, background_color='#404a59')
        flag = True
        # 创建城市与对应数量的列表数据
        data = [(city_com['city'][i], city_com['count'][i]) for i in range(0, city_com.shape[0])]
        while flag:
            # 转换数据序列，将带字典和元组类型的序列转换为 k_lst,v_lst 两个列表
            attr, value = geo.cast(data)
            try:
                # 添加城市热点图
                # attr城市名称、value对应数量、type类型、visual_range热点区间值、visual_text_color字体颜色
                # is_visualmap是否为视觉地图、
                geo.add("", attr, value, type="heatmap", visual_range=[0, 50], visual_text_color="#fff",
                        is_visualmap=True)
                flag = False     # 修改循环标记
            except ValueError as e:
                e = str(e)
                e = e.split("No coordinate is specified for ")[1]  # 获取不支持的城市名
                for i in range(0, len(data)):
                    if e in list(data[i]):
                        del data[i]  # 将不支持城市名的数据删除
                        break
                    flag = True
        # 生成全国热力图html文件
        geo.render(d + self.moveName + '全国热力图.html')

        # 通过排序获取数量排行前30的城市信息
        city_main = city_com.sort_values('count', ascending=False)[0:30]
        attr = city_main['city']     # 获取城市名称的数据
        v1 = city_main['count']      # 获取数量
        v2 = city_main['mean']       # 获取平均分
        line = Line("主要城市评分")  # 折线图对象
        # is_stack是否堆叠、xaxis_rotate（x轴城市名称旋转角度）
        # yaxis_min（y轴最小值）
        # mark_point（覆盖物的方式显示最高值和最小值）
        # xaxis_interval（x轴间隔距离，底部显示城市名称之间的距离）
        # line_color（线的颜色）
        # line_width（线宽度）
        # mark_point_textcolor（标记点文字的颜色）
        # is_splitline_show（是否显示分割线）
        line.add("城市", attr, v2, is_stack=True, xaxis_rotate=45, yaxis_min=0,
                 mark_point=['min', 'max'], xaxis_interval=0, line_color='lightblue',
                 line_width=4, mark_point_textcolor='black', mark_point_color='yellow',
                 is_splitline_show=False)    # 添加折线图
        bar = Bar("主要城市评论数")          # 柱形图对象
        bar.add("城市", attr, v1, is_stack=False, xaxis_rotate=45, yaxis_min=0,
                xaxis_interval=0, is_splitline_show=False,mark_point_color='yellow')   # 添加柱形图
        overlap = Overlap()    # 叠加图表对象
        # 默认不新增 x y 轴，并且 x y 轴的索引都为 0
        overlap.add(bar)
        overlap.add(line, yaxis_index=1, is_add_yaxis=True)
        # 生成主要城市评论数_平均分.html文件
        overlap.render(d + self.moveName+'主要城市评论数_平均分.html')

        # 获取评论内容
        tomato_str = ' '.join(tomato_com['comment'])
        words_list = []  # 保存词汇的列表
        # 分词
        word_generator = jieba.cut_for_search(tomato_str)
        for word in word_generator:
            words_list.append(word)  # 将拆分后的词汇添加至列表当中
        words_list = [k for k in words_list if len(k) > 1]  # 筛选词汇长度大于1的
        back_color = imageio.imread(d + '词云背景.jpg')  # 读取图片
        wc = WordCloud(background_color='white',  # 背景颜色
                       max_words=200,  # 最大词数
                       mask=back_color,  # 以该参数值作图绘制词云，这个参数不为空时，width和height会被忽略
                       max_font_size=300,  # 显示字体的最大值
                       font_path="STFANGSO.ttf",  # 字体
                       random_state=42,  # 为每个词返回一个PIL颜色
                       # width=1000,  # 图片的宽
                       # height=860  # 图片的长
                       )
        tomato_count = collections.Counter(words_list)  # 统计数量
        wc.generate_from_frequencies(tomato_count)  # 生成词云图
        # 基于彩色图像生成相应彩色
        image_colors = ImageColorGenerator(back_color)
        # 创建图形
        plt.figure()
        # 显示彩色图像
        plt.imshow(wc.recolor(color_func=image_colors))
        # 去掉坐标轴
        plt.axis('off')
        # 保存词云图片
        wc.to_file(path.join(d, self.moveName + '词云.png'))
        pass

    #  为查看按钮绑定事件的方法
    def btnclick(self):
        self.pushButton_2.clicked.connect(self.reli2)
        self.pushButton_3.clicked.connect(self.reli3)
        self.pushButton_4.clicked.connect(self.reli4)
    #  主要城市评论数-及平均分查看按钮事件
    def reli2(self):
        # 创建显示对应图表的窗体对象
        win.kk(self.moveName+'主要城市评论数及平均分',self.moveName+'主要城市评论数_平均分.html')
        win.show()   # 显示窗体

    #  全国热力图查看按钮事件
    def reli3(self):
        win.kk(self.moveName + '全国热力图', self.moveName + '全国热力图.html')
        win.show()

    # 词云 查看按钮事件
    def reli4(self):
        winy.kk(self.moveName + '词云', self.moveName + '词云.png')
        winy.show()

if __name__ == '__main__':
    d = os.path.dirname(os.path.realpath(sys.argv[0])) + "/"  # 获取当前文件所在路径
    d = re.sub(r'\\', '/', d)  # 将路径中的分隔符\替换为/
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    # 显示热力图，主要城市评论数_平均分窗体
    win = MainWindows()
    # 显示云图窗体
    winy = MainWindowy()
    ui = Ui_Form()   # 初始化窗体
    ui.setupUi(MainWindow)
    ui.hide()
    ui.show()
    MainWindow.show()
    sys.exit(app.exec_())