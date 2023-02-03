# urllib基本使用 - 请求对象的定制
import urllib.request

url_page = 'https://www.baidu.com'

# 伪造 headers
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}

# 因为 urlopen 方法中不能存储字典，所以 headers 不能直接作为参数传递，需要定制请求对象
# 注意，因为参数顺序的问题 (Request 需要的三个参数 (url, date=None, headers={}), 中间有个date), 所以需要用关键字传参
request = urllib.request.Request(url=url_page, headers=headers)

response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
print(content)

