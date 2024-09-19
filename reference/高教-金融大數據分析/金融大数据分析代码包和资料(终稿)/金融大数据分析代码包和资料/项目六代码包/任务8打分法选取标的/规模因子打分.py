#引入相关第三方Python库
import pandas as pd
import numpy as np
#读取相关数据
data = pd.read_excel('多因子量化交易/沪深A股.xlsx')

#选取单行业测试
score = data[data['所属申万行业']== '银行']
print(score)

#对总市值进行排序
score_sort = score.sort_values(by = '总市值',ascending=False)

#去除极值
print('上限',score['总市值'].mean()+score['总市值'].std()*3)
a = score['总市值'].mean()+score['总市值'].std()*3
print('下限',score['总市值'].mean()-score['总市值'].std()*3)
b = score['总市值'].mean()-score['总市值'].std()*3

score_sort_1 = score_sort.loc[(score_sort['总市值'].values < a)]    #去除极值
print(len(score_sort_1))    #展示所属行业剩余公司数量

#开始依次进行打分
def score(a):
    quotient = len(a) // 20  # 倍数
    #print(quotient)
    remainder = len(a) % 20  # 余数
    #print(remainder)
    layer = np.array([quotient] * 20)
    #print(layer)

    for i in range(0, remainder):
        layer[-(1 + i)] += 1
    #print(layer)
    layer = np.insert(layer, 0, 0)
    layer = layer.cumsum()
    #print(layer)

    for i in range(0, 20):
        for j in range(layer[i], layer[i + 1]):
            a.iloc[(j, -1)] = i + 1

score(score_sort_1)
print(score_sort_1)

#所有行业循环打分
industry = set(data['所属申万行业'].tolist())
print(industry)

df_empty = pd.DataFrame()
for i in industry: #将行业设置为循环
     #按照总市值倒序排序
    i = pd.DataFrame(data[data['所属申万行业'] == i]).sort_values(by = '总市值',ascending=False)    
    i = i.loc[(i['总市值'].values < i['总市值'].mean() + i['总市值'].std()*3)]    #去除极值
    i['规模因子得分'] = 0       #定义得分，初始分数为0
    score(i)                           #运行此前设置的score函数
    df = pd.DataFrame(i)      #得分结果保存
    df_empty = pd.concat([df_empty,df])        #得分结果添加至df_empty
print (df_empty)                                             #展示结果
df_empty.to_excel('多因子量化交易/结果.xlsx',index=False)   #结果保存至excel文件当中




