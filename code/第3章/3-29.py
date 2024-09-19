# *_* coding : UTF-8 *_*
# 开发团队   ：明日科技
# 开发人员   ：Administrator
# 开发时间   ：2019/4/19  10:52
# 文件名称   ：3-29.py
# 开发工具   ：PyCharm
import pandas  # 导入数据统计模块

# 创建数据
data = {'key': ['a','a','b','c','a'],
        'data': [1,2,3,4,5],
        'data1':[2,4,6,8,10]}
data__frame = pandas.DataFrame(data)  # 创建DataFrame对象

# 创建测试函数
def test_function(data):
    return data.sum()  # 返回求和结果
# 指定函数名称
df = data__frame.agg({'data':test_function})
print(df)      # 打印指定函数名称后的计算结果










