# 一、导入pandas库文件
# 参考操作步骤，将代码书写在下面横线处
import pandas as pd

# 二、读取数据
df = pd.read_excel('数据集成/数据合并/华扬联众_利润表_清洗后.xlsx')
df1 = pd.read_excel('数据集成/数据合并/引力传媒_利润表_清洗后.xlsx')

# 三、数据合并
df= df._append(df1)

# 四、保存数据
df.to_excel('华扬联众与引力传媒利润表合并结果.xlsx', index=False)

# 五、打印数据
print(df)

