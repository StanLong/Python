# urllib基本使用 - urllib 代理
import urllib.request
import urllib.parse

url = 'http://www.baidu.com/s?wd=ip'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}

proxies = {
    'http' : '117.93.180.62:9000'
}

request = urllib.request.Request(url=url, headers= header)
handler = urllib.request.ProxyHandler(proxies=proxies)
opener = urllib.request.build_opener(handler)
response = opener.open(request)
content = response.read().decode('utf-8')

with open('daili.html', 'w', encoding='utf-8') as fp:
    fp.write(content)