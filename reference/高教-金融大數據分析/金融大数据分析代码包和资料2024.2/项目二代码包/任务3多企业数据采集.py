# 一、导入Python库文件
import requests
import pandas as pd

# 二、请输入股票代码、报表年份、报表类型、请求连接
code = [("600000", "浦发银行"),("600036", "招商银行")]
year = ["2020","2021"]
report_period_id = ["5000"]  
url = ["https://ssecurity.seentao.com/debug/security/security.balancesheet.get"]

# 三、使用pandas库文件打开文件
name_file = pd.read_excel('中英指标对照.xlsx', sheet_name='sz_balancesheet')
name_dir = dict(zip(name_file['en'], name_file['ch']))  
data = pd.DataFrame()  

# 四、使用for循环采集数据
try:
    for S_id in code:
        stock_id = S_id[0]
        for b in report_period_id:
            try:
                postdata = {"stockId": stock_id, "reporttype": b, "callType": "collection"}
                json_data = requests.post(url[0], postdata).json()['result']
                df = pd.DataFrame(json_data)
                df = df[df['reportyear'].isin(year)]
                data = pd.concat([data,df])
            except Exception as e:
                print(e)
                continue

    data.rename(columns=name_dir, inplace=True)  
    print(data)
    end_data = data[name_file['ch']]  
    end_data.to_excel('浦发银行&招商银行2020-2021年资产负债表采集结果.xlsx', encoding='utf-8', index=False)  
except Exception as e:
    print('采集失败', e)
