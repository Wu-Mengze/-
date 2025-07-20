#导入必要模块
import requests
import json
from DrissionPage import ChromiumPage
from DrissionPage.common import Actions
from DrissionPage.common import Keys
from pypinyin import pinyin,Style


#定义英文拼音转文字函数
def yuyan(chinese):
    zw = pinyin(chinese,style=Style.NORMAL)
    string = "".join(t[0] for t in zw)
    return string
#定义购票函数
def buy(Go_city,To_city,Sj,Page_num,Phone_number,password,last_4_ID_card):
 zdh = ChromiumPage()
 dzl = Actions(zdh)
 zdh.get("https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=%E6%AD%A6%E6%B1%89,WHN&ts=%E5%8C%97%E4%BA%AC%E5%8C%97,VAP&date=2025-07-20&flag=N,N,Y")
 #出发地点
 dzl.move_to('css:#fromStationText').click().type(yuyan(Go_city))
 zdh.ele('css:#fromStationText').input(Keys.ENTER)
 #到达地点
 dzl.move_to('css:#toStationText').click().type(yuyan(To_city))
 zdh.ele('css:#toStationText').input(Keys.ENTER)
 #出发时间
 zdh.ele('css:#train_date').clear()
 zdh.ele('css:#train_date').input(Sj)
 #查询按钮
 zdh.ele('css:#query_ticket').click()
 #预定按钮#queryLeftTable tr:nth-child(5) td:nth-child(13) .btn72
 zdh.ele(f'css:#queryLeftTable tr:nth-child({2*Page_num-1}) td:nth-child(13) .btn72').click()
 #登录判断
 login = zdh.ele('css:#login_user').text
 if login == "登录":
     #用户名/邮箱/手机号
     zdh.ele('css:#J-userName').input(Phone_number)
     #密码
     zdh.ele('css:#J-password').input(password)
     #登录按钮
     zdh.ele('css:#J-login').click()
     #请输入登录账号绑定的证件号（身份证）后4位
     zdh.ele('css:#id_card').input(last_4_ID_card)
     #发送验证码
     zdh.ele('css:#verification_code').click()
     #验证码
     yzm = int(input("请输入验证码:"))
     zdh.ele('css:#code').input(yzm)
      #确定键
     zdh.ele('css:#sureClick').click()
 else:
     print("已登录")

file_path = r"D:\vscode_all project\python\city.json"
k= open(file_path,encoding='utf-8').read()#读取json文件
city = json.loads(k)

#定义查票交互程序
go_city=input("请输入出发城市:")
to_city=input("请输入到达城市:")
sj = input("请输入出发日期(XXXX-XX-XX):")
phone_number= input("请输入12306绑定的电话号码:")
password = input("请输入12306账号密码:")
last_4_ID_card = input("请输入后四位身份证号码:")
#获取网页
url=f"https://kyfw.12306.cn/otn/leftTicket/queryU?leftTicketDTO.train_date={sj}&leftTicketDTO.from_station={city[go_city]}&leftTicketDTO.to_station={city[to_city]}&purpose_codes=ADULT"
headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0",
           "cookie":"JSESSIONID=E35AAB2567CB61E69E28F002B9FB39BF; _jc_save_wfdc_flag=dc; guidesStatus=off; highContrastMode=defaltMode; cursorStatus=off; _jc_save_fromStation=%u6B66%u6C49%2CWHN; BIGipServerotn=1742274826.64545.0000; BIGipServerpassport=870842634.50215.0000;",
           "referer":"https://kyfw.12306.cn/otn/leftTicket/init?"}#注意cookie更新

res = requests.get(url,headers = headers)
print(res.status_code)
JSON = res.json()
date = JSON['data']['result']
#寻找每一个列车信息
page_num= 1

for i in date :
     index = i.split('|')
     train = index[3]
     start_time = index[8]
     end_time = index[9]
     all_time = index[10]
     vip_seat = index[32]
     yrz = index[31]
     edz = index[30]

     dit = {
        "序号":page_num,
        "车次":train,
        "发车时间":start_time,
        "到站时间":end_time,
        "行驶时间":all_time, 
        "商务座位":vip_seat, 
        "一等座":yrz, 
        "二等座":edz 
     }
     print(dit)
     page_num+=1

page_num = input("请输入对应的车次序号:")
page_num = int(page_num)
#运行函数
buy(Go_city = go_city,To_city = to_city,Sj = sj,Page_num = page_num,Phone_number=phone_number,password=password,last_4_ID_card=last_4_ID_card)