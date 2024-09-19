# *_* coding : UTF-8 *_*
# 开发团队   ：明日科技
# 开发人员   ：Administrator
# 开发时间   ：2019/4/19  14:30
# 文件名称   ：3-32.py
# 开发工具   ：PyCharm
import pandas  # 导入数据统计模块

# 创建数据
data = {'A': ['A1','A2','A3'],
        'B': ['B1','B2','B3'],
        'C':['C1','C2','C3']}
data1 = {'C': ['C4','C2','C3'],
        'D': ['D1','D2','D3'],
        'E':['E1','E2','E3']}
data__frame = pandas.DataFrame(data)  # 创建DataFrame对象
data__frame1 = pandas.DataFrame(data1)  # 创建DataFrame1对象
# 打印合并后数据
print(pandas.merge(data__frame,data__frame1,how='outer',on='C'))
