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
def buy(Go_city,To_city,Sj,Page_num):
 zdh = ChromiumPage()
 dzl = Actions(zdh)
 zdh.get('https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=%E6%AD%A6%E6%B1%89%E4%B8%9C,LFN&ts=%E5%B9%BF%E5%B7%9E%E8%A5%BF,GXQ&date=2025-05-24&flag=N,N,Y')

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
 #预定按钮
 zdh.ele(f'css:#queryLeftTable tr:nth-child({int(Page_num)*2-1}) .btn72').click()
 #登录判断
 login = zdh.ele('css:#login_user').text
 if login == "登录":
     #用户名/邮箱/手机号
     zdh.ele('css:#J-userName').input("13307112080")
     #密码
     zdh.ele('css:#J-password').input("wuzhen19861088")
     #登录按钮
     zdh.ele('css:#J-login').click()
     #请输入登录账号绑定的证件号（身份证）后4位
     zdh.ele('css:#id_card').input("8532")
     #发送验证码
     zdh.ele('css:#verification_code').click()
     #验证码
     yzm = int(input("请输入验证码:"))
     zdh.ele('css:#code').input(yzm)
      #确定键
     zdh.ele('css:#sureClick').click()
 else:
     print("已登录")

k= open('D:\\vscode_all project\\网络爬虫\\city.json',encoding='utf-8').read()#读取json文件
city = json.loads(k)

#定义查票交互程序
go_city=input("请输入出发城市:")
to_city=input("请输入到达城市:")
sj = input("请输入出发日期:")

#获取网页
url=f"https://kyfw.12306.cn/otn/leftTicket/queryU?leftTicketDTO.train_date={sj}&leftTicketDTO.from_station={city[go_city]}&leftTicketDTO.to_station={city[to_city]}&purpose_codes=ADULT"
headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0",
           "cookie":"tk=bZMRUTTy5kk7E8NwmzaKemcV5_jMritcLned6Anxe1e0; JSESSIONID=D1C10ABDD1D8E56C6561AE24FA7585F9; _jc_save_toDate=2025-05-24; _jc_save_wfdc_flag=dc; guidesStatus=off; highContrastMode=defaltMode; cursorStatus=off; _jc_save_fromDate=2025-05-24; _jc_save_fromStation=%u6B66%u6C49%u4E1C%2CLFN; _jc_save_toStation=%u5E7F%u5DDE%u897F%2CGXQ; route=c5c62a339e7744272a54643b3be5bf64; BIGipServerotn=1507393802.50210.0000; BIGipServerpassport=803733770.50215.0000",
           "referer":"https://kyfw.12306.cn/otn/leftTicket/init?"}#注意cookie更新

page_num = 0 #循环列表
res = requests.get(url,headers = headers)
print(res.status_code)
JSON = res.json()
date = JSON['data']['result']
#寻找每一个列车信息
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
buy(Go_city = go_city,To_city = to_city,Sj = sj,Page_num = page_num)#运行函数