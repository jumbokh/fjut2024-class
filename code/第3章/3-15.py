# *_* coding : UTF-8 *_*
# 开发团队   ：明日科技
# 开发人员   ：Administrator
# 开发时间   ：2019/4/19  11:37
# 文件名称   ：3-15.py
# 开发工具   ：PyCharm
import pandas  # 导入数据统计模块

data = {'A': [1, 2, 3, 4, 5],
        'B': [6, 7, 8, 9, 10],
        'C':[11,12,13,14,15]}
data__frame = pandas.DataFrame(data)  # 创建DataFrame对象
data__frame['B'] = [5,4,3,2,1]        #  将B列中所有数据修改
print(data__frame)                       # 打印DataFrame对象内容
