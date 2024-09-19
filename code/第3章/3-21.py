# *_* coding : UTF-8 *_*
# 开发团队   ：明日科技
# 开发人员   ：Administrator
# 开发时间   ：2019/4/19  13:32
# 文件名称   ：3-21.py
# 开发工具   ：PyCharm
import pandas as pd    # 导入pandas模块

# 设置起始时间为'1/1/2019'，periods指定的时间范围为48小时，freq设置以小时为间隔
rng = pd.date_range('1/1/2019', periods=24, freq='H')
data = {'time':rng} # 创建时间数据
data_frame = pd.DataFrame(data) # 生成时间数据的DataFrame对象
print('时间数据的类型为：',type(data_frame['time'][0]))
y = [i.year for i in data_frame['time']]   # 获取时间数据中所有年份
print('获取时间数据中的所有年份：',y)      # 打印获取时间数据中所有年份
