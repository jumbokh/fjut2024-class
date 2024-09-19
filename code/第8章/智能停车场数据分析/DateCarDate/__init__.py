# 停车场数据生成
from util.CarNumber import *
from util.TimeUtil import *
import random
import pandas as pd
from pandas import DataFrame
import os
# 总车位数
Total=100
# 获取文件的路径
cdir = os.getcwd()
# 文件路径
path=cdir+'/datafile/'
# 读取路径
if not os.path.exists(path):
    # 根据路径建立文件夹
    os.makedirs(path)
    # 车牌号 进停车场时间 出停车场时间  价格 状态（进车\出车）   当前剩余车位数
    carnfile = pd.DataFrame(columns=['cn','timein' ,'timeout', 'price', 'state','rps'])
    # 生成xlsx文件
    carnfile.to_excel(path+'停车场信息表.xlsx', sheet_name='data',index=False)
# 读取文件内容
pi_table = pd.read_excel(path+'停车场信息表.xlsx', sheet_name='data')

# 停车场数据格式:
# 编号  车牌号 时间  状态（进车\出车） 价格  当前剩余车位数
# 自定义模块：时间,格林威治时间互相转换模块，生成车牌号模块
# 数据插入程序：
# 时间循环
#   是否插入数据随机（让每天进出车数据条数为大概1/600 大体10分钟更新一条数据）:
#         第一次插入数据 进车：
#              随机车牌号
#              剩余车位-1
#              插入数据（ 时间  车牌号 进车标识 价格0 当前剩余车位数）
#         不是第一次插入数据随机状态：
#              状态-进车：
#                 随机车牌号-排除已经存在文档的车牌号
#                 剩余车位-1
#                 插入数据（ 时间  车牌号 进车标识 价格0 当前剩余车位数）
#              状体-出车：
#                 随机文档中车牌号中的一个
#                 计算收入
#                 剩余车位+1
#                 插入数据（ 时间  车牌号 出车标识 收入价格 当前剩余车位数）

# 数据开始记录时间 2018-03-01 00:00:00
startTime=mktime('2018-01-01 00:00:00')
# 数据结束时间
endTime=mktime('2018-04-01 00:00:00')
print('添加数据')
# 根据时间戳循环时间
for i in  range(startTime,endTime):
    # 设置更新数据概率1/600 因为按照秒数循环大体10分钟更新一条数据
    if random.randint(0, 600)==1:
       # print('进入1/600')
       # print(localtime(i))
       # 判断数据表中是否有数据
       # 停车场车辆
       cars = pi_table[['cn','timein' ,'timeout', 'price', 'state','rps']].values
       # 已进入车辆数量
       carn = len(cars)
       if carn == 0:

           # 随机获取车牌号
           cn=carNumber()
           # 根据时间戳获取时间
           timein=localtime(i)
           # 车位-1
           Total=Total-1
           # 添加信息到文档 ['cn','timein' ,'timeout', 'price', 'state','rps']
           pi_table = pi_table.append({'cn': cn,
                                       'timein': timein,
                                       'timeout': 0,
                                       'price': 0,
                                       'state': 0,
                                       'rps': Total}, ignore_index=True)
           # 更新xlsx文件
           DataFrame(pi_table).to_excel(path + '停车场信息表.xlsx',
                                        sheet_name='data', index=False, header=True)
           print('第一次数据',pi_table)
           pass
       else:

           # cars = pd.read_excel(path + '停车场信息表.xlsx', skiprows=carn - 1, sheet_name='data').values
           # # 循环文档信息
           # for car in cars:
           #      Total=car[5]

           # 判断进车还是出车 0代表进车库车量
           if random.randint(0, 1) == 0:
               # 车位-1
               Total = Total - 1
               if Total == -1:
                   print('停车位已满')
                   continue
               # 随机获取车牌号
               cn = carNumber()
               # 根据时间戳获取时间
               timein = localtime(i)
               # 添加信息到文档 ['cn','timein' ,'timeout', 'price', 'state','rps']
               pi_table = pi_table.append({'cn': cn,
                                           'timein': timein,
                                           'timeout': 0,
                                           'price': 0,
                                           'state': 0,
                                           'rps': Total}, ignore_index=True)
               # 更新xlsx文件
               DataFrame(pi_table).to_excel(path + '停车场信息表.xlsx',
                                            sheet_name='data', index=False, header=True)
               print('进车数据',pi_table)
               cars = pi_table[pi_table['state'] == 0].values
               if len(cars) == 0:
                   Total = 100
                   continue
               car = random.choice(cars)
               timein = car[1]
               # 根据时间戳获取时间
               timeout = localtime(i)
               h = DtCalc(mktime(timein), mktime(timeout))  # 计算时间
               if h >= 12:
                   Total=Total+1
                   pi_table.loc[pi_table['cn'] == car[0], ['timeout']] = timeout
                   pi_table.loc[pi_table['cn'] == car[0], ['state']] = 1
                   pi_table.loc[pi_table['cn'] == car[0], ['price']] = h * 3
                   pi_table.loc[pi_table['cn'] == car[0], ['rps']] = Total
                   # 更新xlsx文件
                   DataFrame(pi_table).to_excel(path + '停车场信息表.xlsx',
                                                sheet_name='data', index=False, header=True)

                   print('出车后数据', pi_table)
                   pass
               pass
           # 1代表出车库车辆
           else:
               print('出车')
               # 车位
               Total = Total + 1
               if Total == 101:
                   print('停车场中没有车辆')
                   Total=100
                   continue
               cars = pi_table[pi_table['state'] ==0].values
               if len(cars)==0:
                   Total=100
                   continue
               car =random.choice(cars)
               print('出车车牌号',car[0])
               # 随机获取车牌号
               cn = car[0]
               timein = car[1]
               # 根据时间戳获取时间
               timeout = localtime(i)
               h=DtCalc(mktime(timein), mktime(timeout))
               pi_table.loc[pi_table['cn'] == car[0], ['timeout']] = timeout
               pi_table.loc[pi_table['cn'] == car[0], ['state']] = 1
               pi_table.loc[pi_table['cn'] == car[0], ['price']] = h*3
               pi_table.loc[pi_table['cn'] == car[0], ['rps']] = Total

               # # 添加信息到文档 ['cn','timein' ,'timeout', 'price', 'state','rps']
               # pi_table = pi_table.append({'cn': cn,
               #                             'timein': timein,
               #                             'timeout': timeout,
               #                             'price': h*3,
               #                             'state': 1,
               #                             'rps': Total}, ignore_index=True)
               # 更新xlsx文件
               DataFrame(pi_table).to_excel(path + '停车场信息表.xlsx',
                                            sheet_name='data', index=False, header=True)
               print('出车后数据',pi_table)
               pass
       pass
print('结束添加数据')
