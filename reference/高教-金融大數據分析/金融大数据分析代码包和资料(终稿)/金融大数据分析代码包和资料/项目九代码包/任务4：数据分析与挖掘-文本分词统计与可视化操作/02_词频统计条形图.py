import jieba
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号

txt = open("货币政策文本分析/19Q2.txt",'r',encoding='utf-8').read()
jieba.load_userdict("货币政策文本分析/dic.txt")

count = jieba.cut(txt)
word_count={}

stopwords = [line.strip() for line in open("货币政策文本分析/stop.txt",'rb').readlines()]

#建立计数循环
for word in count:
    if word.encode('utf-8') not in stopwords:
        # 不统计字数为一的词
        if len(word) == 1:
            continue
        else:
            word_count[word] = word_count.get(word, 0) + 1
#将计数结果导入至list，并按频率降序进行排序
items = list(word_count.items())
items.sort(key=lambda x: x[1], reverse=True)
items = items[0:15:1]#截取出现频率最高的前15个词汇
print(items)

def dic_to_csv(dic_data):
    pd.DataFrame(dic_data).to_csv('词频统计结果_19Q2.csv', encoding='utf-8-sig',header = ['词汇','出现频率'],index = False)
dic_to_csv(items)
#对结果进行可视化展示
data = pd.read_csv(r'词频统计结果_19Q2.csv',encoding = 'utf-8-sig')#读取数据
#设置绘图风格
plt.style.use('ggplot')

#绘制条形图
plt.bar(x = range(data.shape[0]),  #指定条形图x轴的刻度值(有的是用left，有的要用x)
        height = data.出现频率,  #指定条形图y轴的数值（python3.7不能用y，而应该用height）
        tick_label = data.词汇,  #指定条形图x轴的刻度标签
        color = 'steelblue')#指定条形图的填充色
#添加y轴的标签
plt.ylabel('次数')
#添加条形图的标题
plt.title('报告词频次数统计')
#为每个条形图添加数值标签
for x,y in enumerate(data.出现频率):
    plt.text(x,y+0.1,"%s"%round(y,1),ha='center')  #round(y,1)是将y值四舍五入到一个小数位
plt.xticks(rotation=50)
#显示图形
plt.show()
