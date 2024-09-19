import matplotlib.pyplot as plt    # 导入绘图模块
import matplotlib                  # 导入图表模块
# 避免中文乱码
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False
# 创建图形画布对象
fig = plt.figure()
# 模拟数据
x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [1, 3, 2, 1, 6, 2, 4, 6]
# 设置子区域x1绘制位置与大小
left, bottom, width, height = 0.1, 0.1,0.8,0.8
# 添加子区域x1
x1 = fig.add_axes([left, bottom, width, height])
x1.plot(x, y, 'b')     # 绘制子区域x1图表，设置子区域x1折线颜色为蓝色
x1.set_title('子图x1') # 设置子区域x1图表标题文字

# 设置子区域x2绘制位置与大小
left, bottom, width, height = 0.2, 0.5, 0.25, 0.25
# 添加子区域x2
x2 = fig.add_axes([left, bottom, width, height])
x2.plot(x, y, 'y')     # 绘制子区域x2图表，设置子区域x2折线颜色为黄色
x2.set_title('子图x2') # 设置子区域x2图表标题文字
plt.show()             # 显示图表
