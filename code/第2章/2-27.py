from numpy import matlib  # 导入矩阵子模块

# empty函数中参数shape为指定矩阵的形状、参数dtype为数据类型、order为C时（行序优先）F（列序优先）
print('随机数矩阵：\n',matlib.empty((3,3),dtype='int32'))   # 打印创建的随机数矩阵
print('以数字1填充的矩阵：\n',matlib.ones((3,3)))           # 打印创建以数字1填充的矩阵
print('以数字0填充的矩阵：\n',matlib.zeros((3,3)))          # 打印创建以数字0填充的矩阵
# 打印创建对角线为1的矩阵，其中参数n为行数、M为列数、k为对角线索引、dtype为数据类型
print('对角线为1的矩阵：\n',matlib.eye(n=3,M=3,k=0,dtype=int))