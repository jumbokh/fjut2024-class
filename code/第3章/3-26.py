# *_* coding : UTF-8 *_*
# 开发团队   ：明日科技
# 开发人员   ：Administrator
# 开发时间   ：2019/4/19  13:54
# 文件名称   ：3-26.py
# 开发工具   ：PyCharm
import pandas  # 导入数据统计模块

# 创建数据
data = {'key': ['a','a','b','c','a'],
        'data': [1,2,3,4,5],
        'data1':[2,4,6,8,10]}
data__frame = pandas.DataFrame(data)  # 创建DataFrame对象
# 仅根据key进行分组
group = data__frame.groupby(data__frame['key'])
# 循环迭代分组数据
for a in group:
        print('分组数据迭代后为：\n',a)
