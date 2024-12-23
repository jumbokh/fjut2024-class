import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

aa =r'.\data\JDdata.xls'
bb=r'.\data\JDcar.xls'
resultfile1=r'result1.xls'
resultfile2=r'result2.xls'
dfaa = pd.DataFrame(pd.read_excel(aa))
dfbb=pd.DataFrame(pd.read_excel(bb))
df1=dfaa[['业务日期','金额']]
df2=dfbb[['投放日期','支出']]

#去除空日期和金额为0的记录
df1=df1[df1['业务日期'].notnull() & df1['金额'] !=0]
df2=df2[df2['投放日期'].notnull() & df2['支出'] !=0]

df1['业务日期'] = pd.to_datetime(df1['业务日期'])
df2['投放日期'] = pd.to_datetime(df2['投放日期'])

dfData = df1.set_index('业务日期',drop=True)
dfCar=df2.set_index('投放日期',drop=True)

# 按月度统计并显示销售金额
dfData_month=dfData.resample('M').sum().to_period('M')
# 按月度统计并显示广告费支出金额
dfCar_month=dfCar.resample('M').sum().to_period('M')

dfData_month.to_excel(resultfile1) #导出结果
dfCar_month.to_excel(resultfile2) #导出结果

clf=linear_model.LinearRegression(fit_intercept=True,normalize=False)
#x为广告费用，y为销售收入
x=pd.DataFrame(dfCar_month['支出'])
y=pd.DataFrame(dfData_month['金额'])

# 图表字体为华文细黑，字号为10
plt.rc('font', family='SimHei', size=10)
plt.figure("销售收入分析")
plt.scatter(x, y,  color='red') #真实值散点图
#plt.show()

#绘制拟合图
clf.fit(x,y) #拟合线性模型
k=clf.coef_ #获取回归系数（斜率w1,w2,w3,...,wn）
b=clf.intercept_ #获取截距w0

#7月预计投入60000元广告费（x0）
x0=60000
#预测7月销售收入（y0），y0=截距+X值*斜率
y0=b+x0*k
print(y0)

#使用线性模型进行预测y值
y_pred =clf.predict(x)

plt.plot(x,y_pred, color='blue', linewidth=1.5) #预测回归线
plt.ylabel(u'销售收入（元）')
plt.xlabel(u'广告费（元）')
plt.show()


