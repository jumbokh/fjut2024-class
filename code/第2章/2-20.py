import numpy as np                # 导入numpy模块

a = np.array([0,30,60,90])         # 模拟不同角度的数组
print('正弦弧度为：',np.sin(a))    # 打印正弦弧度
print('正弦值为：',np.sin(a*np.pi/180)) # 打印正弦值
print('余弦值为：',np.cos(a*np.pi/180)) # 打印余弦值
print('正切值为：',np.tan(a*np.pi/180)) # 打印正切值
print('斜边值为：',np.hypot(13,12))     # 打印斜边值，根据已知两个边的值计算斜边值
arcsin = np.arcsin(np.sin(a*np.pi/180)) # 反正弦弧度，参数为正弦值
print('反正弦弧度为',arcsin)            # 打印反正弦弧度
print('反正弦弧度转换为度：',np.degrees(arcsin)) # 打印反正弦弧度转换为角度
print('角度转换为弧度：',np.radians(a))          # 打印角度转换为弧度
print('弧度转换为角度：',np.rad2deg(np.radians(a))) # 打印弧度转换为角度