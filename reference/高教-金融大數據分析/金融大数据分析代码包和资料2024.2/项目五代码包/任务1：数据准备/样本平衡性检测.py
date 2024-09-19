# -*- coding:utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['simhei']
mpl.rcParams['axes.unicode_minus'] = False


df = pd.read_csv('信用卡欺诈检测/数据来源/信用卡数据.csv',engine="python",encoding="utf-8")
print(df.head())
fig,ax = plt.subplots(dpi=600)
df['交易是否具有欺诈性'].value_counts().plot(ax = ax, kind = 'bar', ylabel = '样本数', xlabel='样本标签')
plt.show()
print(df['交易是否具有欺诈性'].value_counts())