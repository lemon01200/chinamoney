# from lzx
import json
import requests
import csv

url = "https://iftp.chinamoney.com.cn/ags/ms/cm-u-bond-md/BondMarketInfoListEN"
headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0",
    "Cookie" : "AlteonP10=AKUkMiw/F6x7XA1qg1y/Wg$$; apache=4a63b086221745dd13be58c2f7de0338; ags=a23ede7e97bccb1b2380be21609ada80; _ulta_id.ECM-Prod.ccc4=ad50dc8fb4923a77; _ulta_ses.ECM-Prod.ccc4=632a201de22bee53",
    "Host": "iftp.chinamoney.com.cn"
}
# 定义表单数据
data = {"bondType": "100001",
        "issueYear": 2023,
        "pageNo": 1,
        "pageSize": 15}

# 发生post请求
response = requests.post(url, data=data,headers=headers)

# 检查响应状态
if response.status_code == 200:
    # 获取请求数据
    response_json = json.loads(response.text)
    datas = response_json["data"]['resultList']
    csv_file = "./data.csv"

    # 设置映射变量
    field_mapping = {"isin": "ISIN",
                     "bondCode": "Bond Code",
                     "entyFullName": "Issuer",
                     "bondType": "Bond Type",
                     "issueEndDate": "Issue Date",
                     "debtRtng": "Latest Rating"}

    # 写入 CSV 文件
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=field_mapping.values())

        # 写入表头
        writer.writeheader()

        # 过滤并写入数据
        for item in datas:

            filtered_item = {field_mapping[key]: item[key] for key in list(field_mapping.keys()) if key in item}
            writer.writerow(filtered_item)

    print(f"数据已成功写入 {csv_file}")

else:
    print('请求失败，状态码:', response.status_code)
