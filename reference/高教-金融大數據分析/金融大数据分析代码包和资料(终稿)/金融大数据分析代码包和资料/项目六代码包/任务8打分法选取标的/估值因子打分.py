#引入相关第三方Python库
import pandas as pd
import numpy as np
#读取相关数据
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

#所有行业循环打分
industry = set(data['所属申万行业'].tolist())
df_empty = pd.DataFrame()
for i in industry:#将行业设置为循环
    # 按照动态市盈率倒序排序
    i = pd.DataFrame(data[data['所属申万行业'] == i]).sort_values(by = '动态市盈率',ascending=False)
    i = i.loc[(i['动态市盈率'].values < i['动态市盈率'].mean() + i['动态市盈率'].std()*3)] #去除极值
    i['估值因子得分'] = 0     #定义得分，初始分数为0
    score(i)                #运行此前设置的score函数
    df = pd.DataFrame(i)    #得分结果保存
    df_empty = pd.concat([df_empty,df])        #得分结果添加至df_empty
print (df_empty)            #展示结果
df_empty.to_excel('多因子量化交易/结果.xlsx',index=False) #结果保存至excel文件当中