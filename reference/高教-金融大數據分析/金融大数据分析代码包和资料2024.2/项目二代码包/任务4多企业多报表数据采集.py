# 一、导入Python库文件
import requests
import re
import pandas as pd
import time

# 二、请输入股票代码、报表年份、报表类型、请求连接
code = [("600000", "浦发银行"), ("600036", "招商银行")]
year = ["2020", "2021"]
report_period_id = ["5000"]
url = ["https://ssecurity.seentao.com/debug/security/security.balancesheet.get",
       "https://ssecurity.seentao.com/debug/security/security.incomestatement.get"]

# 三、配置输出数据文件名翻译对照字典
name_dict = {"incomestatement": "利润表", "cashflow": "现金流量表", "balancesheet": "资产负债表"}

# 四、使用for循环采集数据
try:
    for one in url:
        name = re.search('\/security\.(.*)\.get', one).group(1)
        sheet_name = 'sz_' + name
        data = pd.DataFrame()
        for S_id in code:
            stock_id = S_id[0]
            for b in report_period_id:
                try:
                    postdata = {"stockId": stock_id, "reporttype": b, "callType": "collection"}
                    json_data = requests.post(one, postdata).json()['result']
                    df = pd.DataFrame(json_data)
                    df = df[df['reportyear'].isin(year)]
                    data = pd.concat([data,df])
                except Exception as e:
                    print(e)
                    continue

        name_file = pd.read_excel('中英指标对照.xlsx', sheet_name=sheet_name)
        name_dir = dict(zip(name_file['en'], name_file['ch']))
        data.rename(columns=name_dir, inplace=True)
        print(data)
        end_data = data[name_file['ch']]
        end_data.to_excel(f"{'&'.join([i[1] for i in code])}_{name_dict.get(name)}采集结果{int(time.time())}.xlsx",
                          encoding='utf-8', index=False)
except Exception as e:
    print('采集失败', e)
