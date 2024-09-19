#导入相关Python库
import pandas as pd
import numpy as np

#设置显示数据全部展示
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)

#读取数据
#df = pd.read_csv('保险精准营销/训练数据.csv')
df = pd.read_excel('保险精准营销/训练数据.xlsx')
#将其他类型变量值转换为数值型
#gender性别变量转换
性别_mapping = {"男": 0, "女": 1}
df['性别'] = df['性别'].map(性别_mapping)

#车辆是否发生过事故变量转换
此前是否发生事故_mapping = {"是": 1, "否": 0}
df['此前是否发生事故'] = df['此前是否发生事故'].map(此前是否发生事故_mapping)

#车辆是否此前购买过保险变量转换
是否购买过车险_mapping = {"是": 1, "否": 0}
df['是否购买过车险'] = df['是否购买过车险'].map(是否购买过车险_mapping)

#车龄信息转换
车龄_mapping = {"> 2 年": 2, "1-2 年": 1, "< 1 年": 0}
df['车龄'] = df['车龄'].map(车龄_mapping)

df.to_excel('保险精准营销/交叉营销数据.xlsx',index = False )