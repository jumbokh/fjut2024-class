#导入相关Python库
import pandas as pd
import numpy as np

#读取上一步骤处理结果数据
data = pd.read_excel('多因子量化交易/结果.xlsx')

#开始依次进行打分
def score(a):
    quotient = len(a) // 20  # 倍数
    #print(quotient)
    remainder = len(a) % 20  # 余数
    #print(remainder)
    layer = np.array([quotient] * 20)
    # print(layer)

    for i in range(0, remainder):
        layer[-(1 + i)] += 1
    # print(layer)
    layer = np.insert(layer, 0, 0)
    layer = layer.cumsum()
    # print(layer)

    for i in range(0, 20):
        for j in range(layer[i], layer[i + 1]):
            a.iloc[(j, -1)] = i + 1


#进行行业循环
industry = set(data['所属申万行业'].tolist())
df_empty = pd.DataFrame()
for i in industry:
    # 按照月涨跌幅正序排序
    i = pd.DataFrame(data[data['所属申万行业'] == i]).sort_values(by = '月涨跌')
    i = i.loc[(i['月涨跌'].values < i['月涨跌'].mean() + i['月涨跌'].std()*3)]    #剔除异常极值数据
    i['动量反转因子得分'] = 0
    score(i)
    df = pd.DataFrame(i)
    df_empty = pd.concat([df_empty,df])    #将输出结果导入至空数据框架
#根据五个因子结果进行求和打分，并输出结果
df_empty['最终得分'] = df_empty['规模因子得分']+ df_empty['估值因子得分'] + df_empty['成长因子得分']+df_empty['盈利因子得分']+df_empty['动量反转因子得分']
df_empty.to_excel('多因子量化交易/结果.xlsx',index=False)

#以行业为分组，选取各行业当中得分最高标的
df2 = df_empty.groupby('所属申万行业').apply(lambda t: t[t.最终得分==t.最终得分.max()])
df2.index = df2.index.droplevel()
df3 = df2.groupby('所属申万行业').apply(lambda t: t[t.估值因子得分==t.估值因子得分.max()])
df3.index = df3.index.droplevel()
df4 = df3.groupby('所属申万行业').apply(lambda t: t[t.盈利因子得分==t.盈利因子得分.max()])
df4.index = df4.index.droplevel()
df5 = df4.groupby('所属申万行业').apply(lambda t: t[t.成长因子得分==t.成长因子得分.max()])
#选取结果输出至选股结果文件当中
df5.to_excel('选股结果.xlsx',index = False)

