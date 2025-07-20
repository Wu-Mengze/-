import requests
import re
from tqdm import tqdm

url = 'https://3cc514d777c6b15f7808dd29b5d8f4d5.v.smtcdns.com/sportsts.tc.qq.com/A8Mm4T5XMzx2_fD7-ncQsTz8_Xjol5fYYyn1XzwyrLk4/B_3k--xdVBUHYl1q0K2jODe-yLlk0rW2NgVFLZiQuS2Kma7ab4A0ZnmOV6wFkAbGEfKzVqTlhGS3Eu06Er4Kj9DRSr67CrZ_vV8I6BjyijFNeAxSgvc13ueNdW2GBfzeLJ9HmSXG3lWBX6Ma0U3ZNrng/svp_50112/_BN16DrDJ00IuAQ082lYugcdCFSsdR4WXzE7TBEyslWGi52yX9R81-TmKQ5UH-G6ZrXaI6oCOLV7JCc16ES6S3Do0b2G3cZUFXvbpj9tapceCagNIoRGnuuqFssuT8xgMB3PU-OUh_A7chOK5HlyCCesqzm-sZKpTWfxhwmowB0pygrZUoEnaQxj95vlXivD2DN-yQuDjPN9yCzwx7ohLNwydYP1c8r8C5ljcad6hzjcMab9j3xwKg/gzc_1000102_0b53nuaboaaa4aaimhzsybuma3odc5fqae2a.f323002.ts.m3u8?ver=4\\'
res = requests.get(url)
print(res.status_code)

text = res.text
date = url.split('gzc')[0]
m3u8 = re.sub("#E.*",'',text)
m3u8_url = m3u8.split()

print("程序正在运行，请稍等")
for t in tqdm(m3u8_url):
    m3u8_ts = date+t
    m3u8_vid = requests.get(m3u8_ts).content
    print(m3u8_ts)
    with open('NBA.mp4','ab') as f:
        f.write(m3u8_vid)
print("成功完成")