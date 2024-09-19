#导入相关Python库
import pandas as pd
import numpy as np
import os
os.environ["PATH"] += os.pathsep + 'D:/软件/Graphviz/bin/' #路径要根据自己的外部软件位置更改！！！！（D:/软件/Graphviz/bin/）

#设置显示数据全部展示
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)

#读取数据
df = pd.read_excel('保险精准营销/交叉营销数据.xlsx')

column_names = df.columns.tolist()

# 列名列表删除“id"和“Response”
column_names.remove('用户ID')
column_names.remove('是否响应')

#构建自变量和因变量
x = df.drop(columns=['是否响应','用户ID'])
y = df['是否响应']

#划分训练集和测试集
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 1 )
#测试集比例为8:2，每次运行代码随机数据固定

# 找到树的最佳深度
# 设定树的深度范围
depth_range = np.arange(1, 20)#设置树身范围在1-20区间
true_score_list = []
test_score_list = []

#调取相关Python库，并建立循环
from sklearn.tree import DecisionTreeClassifier
for d in depth_range:
    clf = DecisionTreeClassifier(max_depth=d).fit(X_train, y_train)
    true_score = clf.score(X_train, y_train)
    true_score_list.append(true_score)
    test_score = clf.score(X_test, y_test)
    test_score_list.append(test_score)

#将树深循环结果进行可视化
import matplotlib.pyplot as plt #调取可视化Python库
plt.figure(figsize=(6, 4), dpi=120 )
plt.grid()
plt.xlabel('max tree deep')
plt.ylabel('score')
plt.plot(depth_range, test_score_list, label='test score')
plt.plot(depth_range, true_score_list, label='train score')
plt.legend()
plt.show()#展示可视化结果

# 获取测试数据集评分最高的索引
te_best_index = int(np.argmax(test_score_list))
# 树的高度=测试数据集评分最高的索引+1
tree_deep = te_best_index + 1
print('树的最佳深度：', tree_deep)

#搭建及训练模型
#调取决策树训练Python库
from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier(max_depth=tree_deep) #设置最大树深为最佳树深
clf = clf.fit(X_train.values,y_train)

#模型预测及评估
#直接预测是否违约
y_pred = clf.predict(X_test.values)
y_pred_proba = clf.predict_proba(X_test.values)
a = pd.DataFrame()  #新建
a['预测值'] = list(y_pred)
a['实际值'] = list(y_test)
#预测响应的概率
y_pred_proba = clf.predict_proba(X_test.values)  #计算响应结果为 0 和 1 时的概率
a['响应概率'] = list(y_pred_proba[:,1])        #截取相应结果为 1 的概率，即用户响应的概率
print(a) #查看真实值、预测值、响应概率

#查看整体预测准确度
from sklearn.metrics import accuracy_score
score = accuracy_score(y_pred,y_test)
print('预测准确度 = ', score)

#模型预测效果评估
from sklearn.metrics import roc_curve
fpr, tpr, thres =roc_curve(y_test.values,y_pred_proba[:,1])
b = pd.DataFrame()
b['阈值'] = list(thres)
b['假警报率'] = list(fpr)
b['命中率'] = list(tpr)
print(b)#查看评估效果
#绘制ROC曲线
plt.rcParams["font.sans-serif"] = [u"SimHei"]#解决中文乱码
plt.rcParams["axes.unicode_minus"] = False #解决负数显示
plt.figure(2)  #新建画布
plt.plot(fpr,tpr, color='red', linewidth=3, linestyle='--')
plt.title('ROC曲线')
plt.xlabel('假提示率')
plt.ylabel('准确率')
plt.show()

#计算变量重要性
importances = pd.DataFrame({'feature': column_names, 'importance': clf.feature_importances_})
importances = importances.sort_values('importance', ascending=False)
importances.to_csv('变量重要性排序.csv', index=False, encoding='utf-8-sig')
print(importances)

from sklearn import tree
import pydotplus

#决策树可视化
# 列出决策树的所有标签，是一个数组
class_names = clf.classes_
# 将标签类型转为str
class_names = [str(i) for i in class_names]

dot_data = tree.export_graphviz(clf, feature_names=column_names,  # 类别名称
                                class_names=class_names,  # 特征名称
                                filled=True)   # 给图形填充颜色
graph = pydotplus.graph_from_dot_data(dot_data)
graph.write_png('决策树.png')  # 保存图像

# 获取预测数据
file_pre = '保险精准营销/预测数据.csv'
df_pre = pd.read_csv(file_pre)
df_pre = df_pre.drop(columns=['用户ID'])# 模型预测
y_predict = clf.predict(df_pre.values)
df_pre['label'] = y_predict
df_pre.to_csv('保险精准营销/预测结果.csv', index=False)