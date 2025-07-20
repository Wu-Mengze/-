from bs4 import BeautifulSoup
import requests
import time

url = 'https://www.avionio.com/widget/en/pkx/departures'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0'
}

res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')

# 获取所有行（作为共同标识）
all_rows = soup.find_all('tr')

print("获取数据中", end="", flush=True)
for i in range(5):
    print(".", end="", flush=True)
    time.sleep(1)

print("\n航班信息如下：")
for row in all_rows:
    # 提取每个字段，找不到则返回空字符串
    try:
        # 航班编号
        plane_num = row.find('td', class_='tt-f').get_text(strip=True) if row.find('td', class_='tt-f') else ""
        
        # 航空公司
        plane_company = row.find('td', class_='tt-al').get_text(strip=True) if row.find('td', class_='tt-al') else ""
        
        # 到达城市
        arrive_city = row.find('td', class_='tt-ap').get_text(strip=True) if row.find('td', class_='tt-ap') else ""
        
        # 日期
        day_time = row.find('td', class_='tt-d').get_text(strip=True) if row.find('td', class_='tt-d') else ""
        
        # 优先查找预计时间，找不到则查找实际时间
        estimated = row.find('td', class_='tt-s sc estimated')
        if not estimated:
            estimated = row.find('td', class_='tt-s sc departed')  
        estimated_time = estimated.get_text(strip=True) if estimated else "未公布"
        
    except AttributeError:
        # 处理可能的解析错误
        continue
    
    # 打印完整行，缺失字段显示默认值
    print(f"航班编号：{plane_num}     航空公司：{plane_company}     到达城市：{arrive_city}     日期：{day_time}     预计/实际时间：{estimated_time}")