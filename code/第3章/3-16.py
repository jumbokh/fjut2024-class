# *_* coding : UTF-8 *_*
# 开发团队   ：明日科技
# 开发人员   ：Administrator
# 开发时间   ：2019/4/19  11:44
# 文件名称   ：3-16.py
# 开发工具   ：PyCharm
import pandas  # 导入数据统计模块

data = {'A': [1, 2, 3, 4, 5],
        'B': [6, 7, 8, 9, 10],
        'C':[11,12,13,14,15]}
data__frame = pandas.DataFrame(data)  # 创建DataFrame对象
print('获取指定行索引范围的数据：',data__frame[0:3])