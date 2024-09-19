# *_* coding : UTF-8 *_*
# 开发团队   ：明日科技
# 开发人员   ：Administrator
# 开发时间   ：2019/4/19  14:05
# 文件名称   ：3-28.py
# 开发工具   ：PyCharm
import pandas  # 导入数据统计模块

# 创建数据
data = {'key': ['a','a','b','c','a'],
        'data': [1,2,3,4,5],
        'data1':[2,4,6,8,10]}
data__frame = pandas.DataFrame(data)  # 创建DataFrame对象
# 获取对data列数据求和，data1求和与列中数据最大值
df = data__frame.agg({'data':'sum','data1':['sum','max']})
print('获取结果为：\n',df)    # 打印获取结果
