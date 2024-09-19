# 引入模块
import time
import datetime
# 时间转换为时间戳
# tss1 = '2013-10-10 23:40:00'
def mktime(tss1):
    # 转为时间数组
    timeArray = time.strptime(tss1, "%Y-%m-%d %H:%M:%S")
    # 转为时间戳
    timeStamp = int(time.mktime(timeArray))
    return timeStamp
# timeStamp=1381419600
def localtime(timeStamp):
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return otherStyleTime  # 2013-10-10 23:40:00
# print(localtime(timeStamp))
# 判断停车时间
# 计算停车时间四舍五入
def DtCalc(stTime, edTime):
    rtn = edTime -stTime
    y=round(rtn/60/60)
    # 判断停车时间 如果时间
    if y == 0:
        y = 1
    return y

# 返回 星期几标记 0代表星期一 1代表星期二...6代表星期天
def get_week_numbeer(date):
    date = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
    day = date.weekday()
    return day