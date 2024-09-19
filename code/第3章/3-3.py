# *_* coding : UTF-8 *_*
# 开发团队   ：明日科技
# 开发人员   ：Administrator
# 开发时间   ：2019/4/19  10:42
# 文件名称   ：3-3.py
# 开发工具   ：PyCharm
import pandas  # 导入数据统计模块

data = ['A','B','C']     # 创建数据数组
index = ['a','b','c']     # 创建索引数组
series = pandas.Series(data,index=index)   # 创建指定索引的Series对象
# 打印下标为0、1、2对应的Series对象
print('获取多个下标对应的Series对象：\n',series[0:3])
