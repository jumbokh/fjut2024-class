# *_* coding : UTF-8 *_*
# 开发团队   ：明日科技
# 开发人员   ：Administrator
# 开发时间   ：2019/4/19  11:09
# 文件名称   ：demo.py
# 开发工具   ：PyCharm
import pandas  # 导入数据统计模块

# 读取Excel文件内容
data = pandas.read_excel('test.xlsx')
# 将读取的信息中指定列，写入新的文件中
data.to_excel('new_test.xlsx',columns=['A','B'],index=False)
new_data = pandas.read_excel('new_test.xlsx',) # 读取新写入的Excel文件信息
print('读取新的Excel文件内容为：\n',new_data)
