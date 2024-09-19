# -*- coding:utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl
plt.rcParams['font.sans-serif'] = ['simhei']  
mpl.rcParams['axes.unicode_minus'] = False 

df = pd.read_csv('信用卡欺诈检测/数据结果/数据清洗结果.csv',engine="python",encoding="utf-8",header=0)
print(df.head())
fig, [[ax1,ax2],[ax3,ax4]] = plt.subplots(2,2, figsize = (15,12), dpi=600)
sns.countplot(x = '交易是否具有欺诈性', hue= '交易是否来自同一零售商', palette='coolwarm', data = df, ax=ax1)
for p in ax1.patches:
    ax1.annotate(p.get_height(), (p.get_x()+0.1, p.get_height()+200))
sns.countplot(x = '交易是否具有欺诈性', hue= '是否通过信用卡进行的交易', palette='coolwarm', data = df,ax=ax2)
for p in ax2.patches:
    ax2.annotate(p.get_height(), (p.get_x()+0.1, p.get_height()+200))
    
sns.countplot(x = '交易是否具有欺诈性', hue= '交易是否使用密码进行', palette='coolwarm', data = df,ax=ax3)
for p in ax3.patches:
    ax3.annotate(p.get_height(), (p.get_x()+0.1, p.get_height()+200))
    
sns.countplot(x = '交易是否具有欺诈性', hue= '交易是否为在线订单', palette='coolwarm', data = df, ax=ax4)
for p in ax4.patches:
    ax4.annotate(p.get_height(), (p.get_x()+0.1, p.get_height()+200))

plt.savefig('信用卡欺诈检测/数据结果/自变量与因变量条形图.png')

fig, [ax1,ax2,ax3,] = plt.subplots(1,3, figsize = (12,8), dpi=600)
sns.boxenplot( x="交易是否具有欺诈性", y="交易离家的距离",  data=df, palette='Blues', ax=ax1)
sns.boxenplot( x="交易是否具有欺诈性", y="距离上一次交易发生地的距离",  data=df, palette='cubehelix', ax=ax2)
sns.boxenplot( x="交易是否具有欺诈性", y="购买价格交易与中位购买价格的比率",  data=df, palette='RdBu_r', ax=ax3)
plt.savefig('信用卡欺诈检测/数据结果/自变量与因变量增强箱图.png')