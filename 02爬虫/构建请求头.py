import urllib.request
import urllib.parse
import ssl

ssl._create_default_https_context = ssl._create_unverified_context # 全局取消 ssl 证书验证

url = 'http://www.baidu.com/'

# 构造伪装的头部
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}

# 构造请求的对象
request = urllib.request.Request(url=url, headers=headers)

# 发送请求
response = urllib.request.urlopen(request)
list = response.getheaders()
for i in list:
    print(i)
# 跟预想的结果不一样， 没在请求头里看到 User-Agent
