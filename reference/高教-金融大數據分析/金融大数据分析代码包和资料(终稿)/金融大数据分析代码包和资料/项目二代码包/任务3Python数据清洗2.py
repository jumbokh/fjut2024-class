import pandas as pd 

file_name = '任务7清洗结果.xlsx'
df = pd.read_excel(file_name)

df = pd.read_excel(file_name)

df[['客户名称', '客户 ID']] = df['客户 ID'].str.split('-', n=1, expand=True)
df[['产品品牌', '品名与规格']] = df['产品名称'].str.split(' ', n=1, expand=True)
df.drop(columns='产品名称', inplace=True)
df['品名与规格'].replace(' ', '', regex=True, inplace=True)
df[['产品品名', '产品规格']] = df['品名与规格'].str.split(',', n=1, expand=True)
df.drop(columns='品名与规格', inplace=True)

df.to_excel('任务8清洗结果.xlsx', index=False)














