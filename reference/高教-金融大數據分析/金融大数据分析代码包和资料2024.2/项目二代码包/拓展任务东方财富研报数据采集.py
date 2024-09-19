# -*- coding:utf-8 -*-
import requests  # 请求库
import json
import re
import os
from lxml import etree
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Host": "data.eastmoney.com",
    "Referer": "http://data.eastmoney.com/report/",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}
def new_folder(name):  # 新建文件夹的函数
    if os.path.exists(f"{name}"):
        return
    else:
        os.mkdir(f"{name}")
def get_page(stockcode):  # 解析网页函数。提取每个pdf的三个信息infocode，title，name并返回
    url = f'http://data.eastmoney.com/report/{stockcode}.html'  
    res = requests.get(url, headers=headers).text
    name = etree.HTML(res).xpath("//div[@id='titlename']/a/text()")[0]  # 提取股票代码对应的中文名 
    new_folder(name)  # 调用new_folder函数   
    res_json = json.loads(re.search(r'var initdata = (.*?\});', res).group(1))  # 将字符串转换为Json并解析
    for one in res_json["data"]:
        info_code, title = one["infoCode"], one["title"]  # 提取出infocode、title信息
        download_pdf(info_code, title, name)  #  调用download_pdf函数
def download_pdf(info_code, title, name):  # 根据传入参数，下载PDF文件到指定路径的函数
    url_midle = 'http://data.eastmoney.com/report/zw_stock.jshtml?infocode=' + info_code 
    con2 = requests.get(url_midle, headers=headers).text
    pdf_url = etree.HTML(con2).xpath(
        "//div[@class='detail-header']/div[@class='report-infos']/span[5]/a/@href")[0]  # 提取PDF文件的链接
    print(pdf_url, title)
    pdf = requests.get(pdf_url)
    with open(f"{name}/{title}.pdf", "wb") as code:
        code.write(pdf.content)  # 下载并保存PDF文件
get_page("601985")  # 传入股票代码，调用函数
print("抓取完成")