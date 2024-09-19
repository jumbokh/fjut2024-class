import numpy as np                # 导入numpy模块

a = np.random.uniform(range(1,6),6) # 产生5个6以内的随机小数
print('原小数数组为：',a)           # 打印原小数数组
print('默认四舍五入后：',np.around(a)) # 打印默认四舍五入后的结果
print('四舍五入右侧一位：',np.around(a,decimals=1))   # 打印四舍五入右侧一位结果
print('四舍五入左侧一位：',np.around(a,decimals=-1))  # 打印四舍五入左侧一位结果
print('最接近的整数',np.rint(a))                      # 打印四舍五入最接近的整数
print('比小数小的最接近整数：',np.floor(a))           # 打印比小数小的最接近整数
print('比小数大的最接近整数：',np.ceil(a))            # 打印比小数大的最接近整数
print('向0舍入到最接近的整数：',np.fix(a))              # 打印向0舍入到最接近的整数