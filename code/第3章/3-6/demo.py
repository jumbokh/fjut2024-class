# *_* coding : UTF-8 *_*
# 开发团队   ：明日科技
# 开发人员   ：Administrator
# 开发时间   ：2019/4/19  10:58
# 文件名称   ：demo.py
# 开发工具   ：PyCharm
import pandas  # 导入数据统计模块

data = pandas.read_csv('test.csv')   # 读取csv文件信息
print('读取的csv文件内容为：\n',data)  # 打印读取的文件内容
