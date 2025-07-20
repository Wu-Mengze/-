import requests
from DrissionPage import ChromiumPage
import re
import os

os.makedirs("Tik Tok video") #创建一个文件夹(注意重名）
#注意cookie更新
headers = {"cookie":"hevc_supported=true; SearchMultiColumnLandingAbVer=2; SEARCH_RESULT_LIST_TYPE=%22multi%22; odin_tt=d2b3562e361612dbf0bf37bfb689b29f97fe83c008f6ebf358d93f7f1630e7303aac1723382878a3a0260db995d717390eaad5a117280167d05aba1190eb4ca0e6dc4285cc312035121c3b62440a2697; UIFID=c8c20d54553eadab8c678961c2b0df95555df87bbc6b890988ad105aec15abc002fcac98690084b1f417817adcf74697d3c9024805e98b49d6fa845d841ca0d66af3710f95fdbb41fb6c573d1586706d359ccd62ab08d626c829a415c06e23e1d9e01f3d5a540a954d271806bdacbd8450ec977a4a5ef388db1d6f86e469700b27eb9bc963c0103ba31e6a68abd13fc3eafe839c0d6a5a1574ed79d36ada8ee3b8f6d9612449ae4f461c9d6ed20017576ae8652e371fafefab3636e69ce27169; passport_csrf_token=9bba3345ebac27aad2e5521133718fc8; passport_csrf_token_default=9bba3345ebac27aad2e5521133718fc8; __security_mc_1_s_sdk_crypt_sdk=40ed52ce-4a0f-b16b; __security_mc_1_s_sdk_cert_key=acf55533-4bde-9eb5; __security_mc_1_s_sdk_sign_data_key_web_protect=806d7ec0-44f4-83b2; bd_ticket_guard_client_web_domain=2; __security_mc_1_s_sdk_sign_data_key_sso=7d169441-46cb-8150; enter_pc_once=1; is_dash_user=1; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Afalse%2C%22volume%22%3A0.065%7D; __live_version__=%221.1.3.5076%22; live_use_vvc=%22false%22; strategyABtestKey=%221751803658.602%22; WallpaperGuide=%7B%22showTime%22%3A1751596712672%2C%22closeTime%22%3A0%2C%22showCount%22%3A1%2C%22cursor1%22%3A16%2C%22cursor2%22%3A4%7D; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1440%2C%5C%22screen_height%5C%22%3A960%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A16%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A50%7D%22; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A1%2C%5C%22is_mute%5C%22%3A0%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A0%7D%22; sdk_source_info=7e276470716a68645a606960273f276364697660272927676c715a6d6069756077273f276364697660272927666d776a68605a607d71606b766c6a6b5a7666776c7571273f275e58272927666a6b766a69605a696c6061273f27636469766027292762696a6764695a7364776c6467696076273f275e582729277672715a646971273f2763646976602729277f6b5a666475273f2763646976602729276d6a6e5a6b6a716c273f2763646976602729276c6b6f5a7f6367273f27636469766027292771273f273c3c3c36363331353d34303234272927676c715a75776a716a666a69273f2763646976602778; bit_env=XEDGfAJQnN16QXgTHS0r55IR-o81iqakqwJYYeDzv_aqDSbdEPkEie0M-I3c1Vor7f2r6aZNBf_SohWx2Y4wdHM5UWnIHpS5pQ4l8wbkbijLDCJE31C_7aU-aj596NJAw4PNSFwxuW9RdfSN8lvWHdM-xbIgpsdOR1VqBbnNHwWT_Szl51Usql5pjc7wT1N_Yghda2kYS08ZsNbc4k5Xzu5vNyinEAKMvvKzeJHkoi53FRMKid7eKQYnrrer-lTSQA1obH1cXADQmvWAj8E_7nV7siJVNKYntJp7bxrQvKBBFyMT0Il_6czk7JRB8RTptUtGZ3APnhc8jVCM4Hcy7rS0ogJPndcX7qN33m6Tw_Fz5eY6JjzTrZfCZ6OabPikr2cm5qeFo-FYQ_ZFswWhBSPiLVL79GerRNmynpSrazVw-Pb2alAuALNH0vaS0TG3C47kcG93Sttv95IrKQ7x8wuV3gT1gJbM3zjPnU7Is_Vi0H-2hsCsPLCCla1TZsbACi31po1C8jm532zqYpD5ffW9kFQ8D2gSvYweyXwD5oo%3D; gulu_source_res=eyJwX2luIjoiNzU0M2ZjOGQ1M2I0ODllM2QzNDA1NDBmYmViY2VhOTQ5YjdkNmE0NmQyY2RiODQzN2RiNDY4OTdiNDkzN2RlZiJ9; passport_auth_mix_state=b2o1891l80srm0rvulnpshp4j2s4pqbq; ttwid=1%7C1ATZ5VnY95HJ1xxrUre8Txs0tk93L6yBLIUT6FXsIPs%7C1751804651%7Cb7822f29c23f94c63f007d48c854b9f0199a63c7d69b5ded9f976f11c51ec258; biz_trace_id=98cd8466; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCTFp2ZkFqbTA4UkY4Q1JteHZ1T2JBb0h1eXYrT0I1eU5qU2Nxdk9vL1ZjZHJJalhVeW45Z21CeDhOb042eVZ5SCsyVFNJMm1CclpYMVNFd3p1c2REcVE9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoyfQ%3D%3D; download_guide=%223%2F20250706%2F0%22; IsDouyinActive=true; home_can_add_dy_2_desktop=%220%22",
           "referer":"https://www.douyin.com/",
           "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0"
           }

Google = ChromiumPage()
Google.listen.start("aweme/post")#监听数据包
Google.get("https://www.douyin.com/user/MS4wLjABAAAAS7hm6jtlJZMAUBAcIoOJPz9RWXeY_ezZxmfIiLT2BiQKr5bwJQjZ-YgrS9N5WDFy")
sjd = Google.listen.wait()#等待数据包加载

#处理监听到的数据包
JSON = sjd.response.body#获取响应数据

data = JSON["aweme_list"]

for i in data:
    video_url = i["video"]["play_addr"]["url_list"][0]
    title = i["desc"]
    title_re = re.sub(r'[<>/?`~_+=.]',"",title)
    res = requests.get(url = video_url,headers=headers).content
    with open("Tik Tok video\\" + title_re + '.mp4','wb') as f:
        f.write(res)