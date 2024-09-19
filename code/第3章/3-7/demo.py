# *_* coding : UTF-8 *_*
# 开发团队   ：明日科技
# 开发人员   ：Administrator
# 开发时间   ：2019/4/19  11:02
# 文件名称   ：demo.py
# 开发工具   ：PyCharm
import pandas  # 导入数据统计模块

data = pandas.read_csv('test.csv')            # 读取csv文件信息
# 将读取的信息中指定列，写入新的文件中
data.to_csv('new_test.csv',columns=['D','E'],index=False)
new_data = pandas.read_csv('new_test.csv')  # 读取新写入的csv文件信息
print('读取新的csv文件内容为：\n',new_data)    # 打印新文件信息
