# urllib基本使用 - 2048核基地(https://bps.jinhaichuang.com/2048/index.php)cookie登录
import urllib.request
import urllib.parse

url = 'https://bps.jinhaichuang.com/2048/u.php?action=show'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'cookie':'zh_choose=n; a22e7_winduser=VFBRXFIFADEAUFYDVwIGVFZYXgBWV1VWAFtTVQdSA1INAwBXVwJUXGo=; a22e7_ck_info=/	; a22e7_ol_offset=46755; a22e7_lastpos=index; a22e7_lastvisit=40	1675866864	/2048/index.php'
    # 'referer' 判断当前路径是不是由上一个路径进来的，一般情况下是做图片防盗链
}

request = urllib.request.Request(url=url, headers= header)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')

with open('2048.html', 'w', encoding='utf-8') as fp:
    fp.write(content)