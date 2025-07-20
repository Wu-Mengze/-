from bs4 import BeautifulSoup
import requests

url = "https://movie.douban.com/top250"
headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0"}

re = requests.get(url, headers = headers)
print(re.status_code)

bs = BeautifulSoup(re.text, 'html.parser')

grid_view=bs.find("ol","grid_view")
all_li=grid_view.find_all("li")

for item in all_li:
    num=item.find("em").text
    str=item.find("span",class_="title").text
    print(f"{num} {str}")
    

