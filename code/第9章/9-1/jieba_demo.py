import jieba   # 导入中文分词模块

'''精确模式示例'''
print('='*30,'精确分词','='*30)
motto = '每一件都要做得精彩绝伦'
word_list = jieba.cut(motto)  # 进行精确模式分词
print('精确模式分词的结果：',word_list)       # 直接输出分词结果
print('精确模式分词的结果：',list(word_list)) # 转换为列表进行输出

'''全模式示例'''
print('\n','='*30,'全分词','='*30)
motto = '每一件都要做得精彩绝伦'
word_list = jieba.cut(motto,cut_all=True)  # 进行全模式分词
print('全模式分词的结果：',list(word_list)) # 转换为列表进行输出

'''搜索引擎模式示例'''
print('='*30,'搜索引擎模式分词','='*30)
motto = '每一件都要做得精彩绝伦'
word_list = jieba.cut_for_search(motto)  # 进行搜索引擎模式分词
print('搜索引擎模式分词的结果：',list(word_list)) # 转换为列表进行输出


