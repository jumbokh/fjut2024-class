#加载文本对比difflib库及可视化库
import difflib
import matplotlib as mpl
#解决中文乱码
mpl.rcParams["font.sans-serif"] = [u"SimHei"]
mpl.rcParams["axes.unicode_minus"] = False
#输入需要进行对比的两个文本
filename1='货币政策文本分析/文本对比_19Q2.txt'
filename2='货币政策文本分析/文本对比_19Q3.txt'

#打开上面输入的文件，逐行进行拆分
with open(filename1,'r',encoding='utf-8', errors='ignore') as f1 , open(filename2,'r',encoding='utf-8', errors='ignore') as f2:
    content1 = f1.read().splitlines(keepends=True)
    content2 = f2.read().splitlines(keepends=True)
#调取difflib进行文本对比，输出文件格式为html
d = difflib.HtmlDiff()
htmlcontent = d.make_file(content1,content2)
with open ('货币政策文本分析/文本对比.html','w',encoding='utf-8') as f:
    f.write(htmlcontent)
    
    
    
    