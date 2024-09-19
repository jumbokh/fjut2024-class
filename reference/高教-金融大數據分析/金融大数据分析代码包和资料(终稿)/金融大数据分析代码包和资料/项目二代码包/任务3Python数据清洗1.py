import pandas as pd

file_name = '数据清洗/Python清洗/01_任务/销售数据_清洗前.xlsx'

df = pd.read_excel(file_name)

df2 = df.replace("-", 0)
df2 = df2.replace(" ", 0)

df2.to_excel('任务7清洗结果.xlsx', index=False)















