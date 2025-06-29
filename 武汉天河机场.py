import requests
import json
import time

# 访问网站
url = "http://www.whairport.com/airport/domPassFlightDepInfo/list.do?pageIndex=1&date=&beginHour=&endHour=&flightNo=&terminal=&airport=&airline=&_=1751170508834"
headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0'
}

# 发送请求并解析数据
res = requests.get(url, headers=headers)
time.sleep(1)
print(f"请求状态码: {res.status_code}")  # 确保请求成功（200）

if res.status_code == 200:
    JSON = res.json()
    data = JSON.get('data', [])  # 安全获取data，默认空列表
    
    # 确认data是列表
    if isinstance(data, list) and len(data) > 0:
        print(f"共获取到 {len(data)} 条航班信息,正在统计",end="",flush=True)
        for i in range(5):
            print(".",end="",flush=True)
            time.sleep(1)
        
        # 定义乘客关心的键（可根据需求增删）
        useful_keys = [
            'fullFlightNo',       # 完整航班号（如MU2126）
            'sdtTime',            # 计划起飞时间
            'estTime',            # 预计起飞时间（可能与计划不同）
            'actTime',            # 实际起飞时间（已起飞时显示）
            'terminal',           # 航站楼（如T3）
            'gateDisp',           # 登机口（如08）
            'releaseStatusNameCn',# 航班状态（如"起飞"、"登机中"）
            'destAirportNameCn',  # 目的地机场（如"西安"）
            'destSdtTime',        # 计划到达时间
            'destEstTime'         # 预计到达时间
        ]
        
        # 筛选每个字典中的有用键值对
        useful_data = []
        for flight in data:  # 遍历每条航班信息（字典）
            # 只保留有用的键，忽略不存在的键（用get避免KeyError）
            filtered_flight = {key: flight.get(key) for key in useful_keys}
            useful_data.append(filtered_flight)
        
        # 打印筛选结果（格式化输出）
        print("\n" + "="*50)
        print(f"{'武汉天河机场航班信息':^50}")
        print("="*50)
        
        for i, flight in enumerate(useful_data):
            print(f"\n航班 {i+1}:")
            print(f"  航班号: {flight.get('fullFlightNo', '无信息')}")
            print(f"  出发地: 武汉天河机场")
            print(f"  目的地: {flight.get('destAirportNameCn', '无信息')}")
            print(f"  计划起飞: {flight.get('sdtTime', '无信息')}")
            print(f"  预计起飞: {flight.get('estTime', '无信息')}")
            print(f"  实际起飞: {flight.get('actTime', '无信息')}")
            print(f"  航站楼: {flight.get('terminal', '无信息')}")
            print(f"  登机口: {flight.get('gateDisp', '无信息')}")
            print(f"  航班状态: {flight.get('releaseStatusNameCn', '无信息')}")
            print(f"  计划到达: {flight.get('destSdtTime', '无信息')}")
            print(f"  预计到达: {flight.get('destEstTime', '无信息')}")
        
        print("\n" + "="*50)
        print(f"统计完毕，共 {len(useful_data)} 条航班信息")
        print("="*50)
    
    else:
        print("data不是有效的列表或为空")
else:
    print("请求失败，无法获取数据")
    



    
    