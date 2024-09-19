# *_* coding : UTF-8 *_*
# 开发团队   ：明日科技
# 开发人员   ：Administrator
# 开发时间   ：2019/4/19  13:24
# 文件名称   ：3-19.py
# 开发工具   ：PyCharm
import pandas  # 导入数据统计模块
import numpy   # 导入numpy模块

data = {'A': [1, 2, 3, 4, 5],
        'B': [6, 7, 8, 9, 10],
        'C':[11,12,13,14,15]}
data__frame = pandas.DataFrame(data)  # 创建DataFrame对象
data__frame['A'][0] = numpy.nan       # 将数据中列名为A行索引为0的元素修改为NaN
print('每列空缺值数量为：\n',data__frame.isnull().sum())     # 打印数据中空缺值数量
print('每列非空缺值数量为：\n',data__frame.notnull().sum())    # 打印数据中非空缺值数量
