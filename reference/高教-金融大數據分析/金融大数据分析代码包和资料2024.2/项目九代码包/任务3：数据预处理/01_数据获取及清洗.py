#导入相关Python库
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal, LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed
import logging
import re

# 不显示warning
logging.propagate = False
logging.getLogger().setLevel(logging.ERROR)

#设置输入及输出文件
pdf_filename = "货币政策文本分析/2023年第一季度中国货币政策执行报告.pdf"
txt_filename = "货币政策文本分析/23Q1.txt"

#创建PDF资源管理器和PDF设备对象，并将资源管理器和设备对象聚合
device = PDFPageAggregator(PDFResourceManager(), laparams=LAParams())
 #创建一个PDF解释器对象
interpreter = PDFPageInterpreter(PDFResourceManager(), device)

# 创建一个PDF文档
doc = PDFDocument()
# 用文件对象来创建一个pdf文档分析器
parser = PDFParser(open(pdf_filename, 'rb'))
# 连接分析器与文档对象
parser.set_document(doc)
doc.set_parser(parser)

# 提供初始化密码，如果没有密码，就创建一个空的字符串
doc.initialize()

# 检测文档是否提供txt转换，不提供就忽略
if not doc.is_extractable:
    raise PDFTextExtractionNotAllowed
else:
    #打开能够进行txt转换的文档，显示文档页数
    with open(txt_filename, 'w', encoding="utf-8") as fw:
        print("num page:{}".format(len(list(doc.get_pages()))))
    
        #建立循环处理每一页的内容
        for page in doc.get_pages():
            interpreter.process_page(page)
            # 接受该页面的LTPage对象
            layout = device.get_result()
            # 这里layout是一个LTPage对象 里面存放着 这个page解析出的各种对象
            for x in layout:
                if isinstance(x, LTTextBoxHorizontal):
                    results = x.get_text()
                    fw.write(results)


# 将刚才输出的 txt 文件重新导入
file = open(txt_filename, encoding='utf-8').read()

# pattern 需要断句的标点符号，这里为逗号“，”和句号“。”
pattern = r'[。]'
file_list = re.split(pattern, file)

# 导出结果覆盖原txt文本文件
with open(txt_filename, 'w+', encoding='utf-8') as file_handle:
    for line in file_list:
        file_handle.write(line.replace("\n", ""))  # 按照pattern断句后，去除掉原本txt的换行符
        file_handle.write("\n")  # 写入新文档时的换行