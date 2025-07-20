import requests
from bs4 import BeautifulSoup as bs


url = 'https://www.cdairport.com/dynamic3.aspx?t=8'
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0'}
res = requests.get(url,headers=headers)
print(res.status_code)

soup = bs(res.text, 'html.parser')

all_rows = soup.find_all('li',class_ = 'clearfix')

for row in all_rows:
    if row is not None:
        text = row.get_text(strip=False)
        print(text)
        
        