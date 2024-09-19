#引入相关第三方Python库
import pandas as pd
import numpy as np
#读取相关数据
data = pd.read_excel('多因子量化交易/沪深A股_pre.xlsx')

#第一步：异常值数据清洗
data = data.drop(data[data.首发上市日期 > '2019-01-01'].index)
data = data.drop(data[data['是否为ST股票'] == '是'].index)
data = data.drop(data[data['是否为*ST股票'] == '是'].index)
data = data.drop(data[data['净资产收益率'] == '——'].index)
print(data)

data.to_excel('多因子量化交易/沪深A股.xlsx')


