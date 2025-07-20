import requests
import json
import time

url = "https://www.szairport.com/szjchbjk/hbcx/flightInfo?type=cn&flag=D&currentDate=1&currentTime=7&hbxx_hbh="
headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0"}
res = requests.get(url,headers=headers)
print(f"正在统计",end="",flush=True)
for i in range(5):
 print(".",end="",flush=True)
 time.sleep(1)

JSON = res.json()
plane = JSON['flightList']
useful_data = []
for flight in plane:
    filtered = {
        '出发时间': flight.get('startSchemeTakeoffTime', '未知'),
        '计划到达时间': flight.get('terminalSchemeLandinTime', '未知'),
        '航班号': [h.get('flightNo', '未知') for h in flight.get('hbh', [])],
        '出发地': flight.get('startStationThreecharcode', '未知'),
        '目的地': flight.get('terminalStationThreecharcode', '未知'),
        '状态': flight.get('fltNormalStatus', '未知')
    }
    useful_data.append(filtered)

# 直接在终端打印
print("筛选后的航班数据：")
for idx, flight in enumerate(useful_data, 1):  # 带序号打印
    print(f"\nlist {idx}:")
    for key, value in flight.items():
        print(f"  {key}: {value}")

