# *_* coding : UTF-8 *_*
# 开发团队   ：明日科技
# 开发人员   ：Administrator
# 开发时间   ：2019/4/19  13:41
# 文件名称   ：3-24.py
# 开发工具   ：PyCharm
import pandas as pd    # 导入pandas模块

# 设置起始时间为'1/1/2019'，periods指定的时间范围为48小时，freq设置以小时为间隔
rng = pd.date_range('1/1/2019', periods=24, freq='H')
data = {'time':rng} # 创建时间数据
data_frame = pd.DataFrame(data) # 生成时间数据的DataFrame对象
# 计算两周零两天前的所有时间
future_time = data_frame['time']-pd.Timedelta(weeks=2,days=2)
print(future_time[:3])          # 打印计算结果的前三位数据
