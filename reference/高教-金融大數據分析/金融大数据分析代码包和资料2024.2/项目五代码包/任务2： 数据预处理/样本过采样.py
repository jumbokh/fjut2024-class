# -*- coding:utf-8 -*-
import pandas as pd
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
df = pd.read_csv('信用卡欺诈检测/数据结果/数据清洗结果.csv',engine="python",encoding="utf-8",header=0)
print(df.head())
X = df.loc[:, df.columns != '交易是否具有欺诈性']
y = df.loc[:, df.columns == '交易是否具有欺诈性']
train_x, test_x, train_y, test_y = train_test_split(X, y, test_size=0.25, random_state=123)
overstamp = SMOTE(random_state=123)
SMOTE_train_x, SMOTE_train_y = overstamp.fit_resample(train_x, train_y)
print(SMOTE_train_y.value_counts())
df_train = pd.concat([SMOTE_train_x, SMOTE_train_y], axis=1)
print(df_train.head())
df_test = pd.concat([test_x, test_y], axis=1)
print(df_test.head())
df_train.to_csv('信用卡欺诈检测/数据结果/训练集数据.csv', index=False, encoding='utf-8-sig')
df_test.to_csv('信用卡欺诈检测/数据结果/测试集数据.csv', index=False, encoding='utf-8-sig')