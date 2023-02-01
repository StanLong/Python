# urllib基本使用 - 下载
import urllib.request

# 下载网页
# url_page = 'http://www.baidu.com'
# urllib.request.urlretrieve(url_page, 'baidu.html') # 参数是是下载路径，参数2是给下载的文件起个名字

# 下载图片
# url_img = 'https://nimg.ws.126.net/?url=https://dingyue.ws.126.net/2021/0329/8ad4eca3j00qqq7cr0064c000u000tim.jpg&thumbnail=650x2147483647&quality=80&type=jpg'
# urllib.request.urlretrieve(url=url_img, filename='jieqi.jpg')

# 下载视频
url_video = 'https://vd3.bdstatic.com/mda-mhkku4ndaka5etk3/sc/cae_h264/1629557146440689988/mda-mhkku4ndaka5etk3.mp4?v_from_s=hkapp-haokan-nanjing&amp;auth_key=1675259913-0-0-5f767ca337e72bc7ed98ace1397f0070&amp;bcevod_channel=searchbox_feed&amp;cd=0&amp;pd=1&amp;pt=3&amp;logid=1712979472&amp;vid=7322829317245497064&amp;abtest=106847_1&amp;klogid=1712979472'
urllib.request.urlretrieve(url=url_video, filename='haokan.mp4')