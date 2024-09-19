# *_* coding : UTF-8 *_*
# 开发团队   ：明日科技
# 开发人员   ：Administrator
# 开发时间   ：2019/4/19  10:50
# 文件名称   ：3-5.py
# 开发工具   ：PyCharm
import pandas  # 导入数据统计模块

data = ['A','B','C']     # 创建数据数组
index = ['a','b','c']     # 创建索引数组
series = pandas.Series(data,index=index)   # 创建指定索引的Series对象
series[0] = 'D'     # 修改下标为0的元素值
print('修改下标为0的元素值：\n',series)  # 打印修改元素值以后的Series对象
series['b'] = 'A'   # 修改索引为b的元素值
print('修改索引为b的元素值：\n',series)  # 打印修改元素值以后的Series对象
