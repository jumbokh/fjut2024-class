# -*- coding:utf-8 -*-
# 一、导入pandas库文件
import pandas as pd

# 二、读取数据
df = pd.read_excel('数据集成/数据关联/销售数据清洗结果.xlsx')
df1 = pd.read_excel('数据集成/数据关联/城市表.xlsx')
df2 = pd.read_excel('数据集成/数据关联/省区表.xlsx')

# 三、数据关联
df = pd.merge(df, df1, how='left', on='城市')
df = pd.merge(df, df2, how='left', on='省/自治区')

# 四、保存数据
df.to_excel('销售数据与销售区域关联结果.xlsx', index=False)

# 五、打印数据
print(df)
