#导入相关Python库：可视化、词云图、分词库；没有库的请在终端安装
import matplotlib.pyplot
import matplotlib.pyplot as plt
import wordcloud
import jieba.analyse

#打开需要进行统计分析的txt文本
f = open("货币政策文本分析/19Q2.txt","r",encoding="utf-8")
t = f.read()
f.close()

#加载分词库和停用词库，截取前100个出现词汇
jieba.load_userdict("货币政策文本分析/dic.txt")
jieba.analyse.set_stop_words("货币政策文本分析/stop.txt")
ls = jieba.analyse.extract_tags(t,topK=100)
txt = " ".join(ls)

#加载字体
myfont = '货币政策文本分析/simkai.ttf'
#建立词云可视化设置并进行词云操作
w = wordcloud.WordCloud(font_path = myfont,\
                        width=1000,height = 700,\
                        background_color="white",\
                        )#设置图片尺寸、背景颜色#
w.generate(txt)

#展示可视化结果，保存图片
plt.imshow(w)
matplotlib.pyplot.show()
w.to_file("词云图19Q2.png")

