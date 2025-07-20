from DrissionPage import ChromiumPage
from DrissionPage.common import Actions

def VIP_get():
 url=input("视频网址:")
 url = str(url)
 zdh = ChromiumPage()
 dzl = Actions(zdh)

 #清除默认内容
 zdh.get('https://jx.xmflv.cc/')
 zdh.ele('css:#url').clear()
 #输入网址
 dzl.move_to('css:#link-area').click().type(url)
 #点击播放
 zdh.ele('css:#bf').click()

VIP_get()
