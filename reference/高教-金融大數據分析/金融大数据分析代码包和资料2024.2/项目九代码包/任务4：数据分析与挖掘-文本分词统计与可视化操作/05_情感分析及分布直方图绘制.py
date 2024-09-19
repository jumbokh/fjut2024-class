#导入相关Python库
from snownlp import SnowNLP
from snownlp import sentiment

#从相应文件夹当中导入文件
source = open("货币政策文本分析/情感分析_20Q2.txt", "r", encoding='utf-8')

#读取文件每行内容，并调用snownlp库进行文本分析
line = source.readlines()
sentimentslist = []
for i in line:
    s = SnowNLP(i)
    print(s.sentiments)
    sentimentslist.append(s.sentiments)

#进行可视化操作
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号

#绘制情绪分布直方图
plt.hist(sentimentslist, bins=np.arange(0, 1, 0.01), facecolor='g')#设置可视化类型
plt.xlabel('情绪指数')#设置x轴标签
plt.ylabel('频率')#设置y轴标签
plt.title('情绪分布直方图')#设置
plt.show()#显示图片