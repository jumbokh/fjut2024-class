# *_* coding : UTF-8 *_*
# 开发团队   ：明日科技
# 开发人员   ：Administrator
# 开发时间   ：2019/4/19  11:25
# 文件名称   ：3-12.py
# 开发工具   ：PyCharm
import pandas  # 导入数据统计模块

data = {'A': [1, 2, 3, 4, 5],
        'B': [6, 7, 8, 9, 10],
        'C':[11,12,13,14,15]}
data__frame = pandas.DataFrame(data)  # 创建DataFrame对象
data__frame.drop([0],inplace=True)  # 删除原数据中索引为0的那行数据
data__frame.drop(labels='A',axis=1,inplace=True) # 删除原数据中列名为A的那列数据
print(data__frame)                    # 打印DataFrame对象内容

