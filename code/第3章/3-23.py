# *_* coding : UTF-8 *_*
# 开发团队   ：明日科技
# 开发人员   ：Administrator
# 开发时间   ：2019/4/19  13:39
# 文件名称   ：3-23.py
# 开发工具   ：PyCharm
import pandas as pd    # 导入pandas模块

# 设置起始时间为'1/1/2019'，periods指定的时间范围为48小时，freq设置以小时为间隔
rng = pd.date_range('1/1/2019', periods=24, freq='H')
data = {'time':rng} # 创建时间数据
data_frame = pd.DataFrame(data) # 生成时间数据的DataFrame对象
result1 = data_frame['time']-data_frame['time']  # 计算两组时间数据的时间差
print('计算两组时间数据的时间差：\n',result1[:3])  # 打印计算结果的前三位数据
# 固定时间的减法运算
result2 = pd.to_datetime('2020 01 01  00:00:00')-data_frame['time']
print('计算结果为：\n',result2[:3])                # 打印计算结果的前三位数据