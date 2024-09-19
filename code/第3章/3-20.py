# *_* coding : UTF-8 *_*
# 开发团队   ：明日科技
# 开发人员   ：Administrator
# 开发时间   ：2019/4/19  13:27
# 文件名称   ：3-20.py
# 开发工具   ：PyCharm
import pandas  # 导入数据统计模块
import numpy   # 导入numpy模块

data = {'A': [1, 2, 3, 4, 5],
        'B': [6, 7, 8, 9, 10],
        'C':[11,12,13,14,15]}
data__frame = pandas.DataFrame(data)  # 创建DataFrame对象
data__frame['A'][0] = numpy.nan       # 将数据中列名为A行索引为0的元素修改为NaN
data__frame.dropna(axis=0,inplace=True)  # 将包含NaN元素所在的整行数据删除
print(data__frame)                            # 打印DataFrame对象内容
