import urllib.request
import urllib.parse

post_url = 'https://fanyi.baidu.com/v2transapi?from=zh&to=en'
query = input('输入要翻译的文字：')
# 构建post表单数据
form_data = {
    "query" : query
}
# 伪装浏览器请求头
headers = {
    "x-requested-with": "XMLHttpRequest",
    "origin": "https://fanyi.baidu.com",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}
# 构建请求对象
request = urllib.request.Request(url=post_url, headers=headers)
# 处理表单数据
form_data = urllib.parse.urlencode(form_data).encode()

# 发送请求
response = urllib.request.urlopen(request, data=form_data)

print(response.read().decode("utf-8"))
# {"errno":997,"errmsg":"\u672a\u77e5\u9519\u8bef","query":"\u8dd1","from":"zh","to":"en","error":997}