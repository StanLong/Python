# urllib基本使用
import urllib.request

# 1. 定义一个url, 就是要访问的地址
url = "http://www.baidu.com"

# 2. 模拟浏览器向服务器发送请求并接收响应
reponse = urllib.request.urlopen(url)

# 3. 获取响应页面中的源码
# read() 返回的是字节形式的二进制数据，需要将二进制的数据转换为字符串，即解码 decode('编码格式')
content = reponse.read().decode('utf-8')

# 4. 打印结果
print(content)
