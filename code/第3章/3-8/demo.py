# *_* coding : UTF-8 *_*
# 开发团队   ：明日科技
# 开发人员   ：Administrator
# 开发时间   ：2019/4/19  11:05
# 文件名称   ：demo.py
# 开发工具   ：PyCharm
import pandas  # 导入数据统计模块

# 读取Excel文件内容
data = pandas.read_excel('test.xlsx')
print('读取的Excel文件内容为：\n', data)
