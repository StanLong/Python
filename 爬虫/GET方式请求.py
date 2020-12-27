import urllib.request
import urllib.parse

word = input('输入搜索条件: ')
url = 'http://www.baidu.com/s?'
# 将参数写成一个字典
data = {
    "wd" : word
}

query_string = urllib.parse.urlencode(data)
url = url + query_string

# 发送请求
response = urllib.request.urlopen(url)
print(response.read().decode('utf-8'))
