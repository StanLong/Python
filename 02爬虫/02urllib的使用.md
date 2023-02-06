# 二、urllib库的使用

## 1. urllib库的使用

```
urllib.request.urlopen()模拟浏览器向服务器发送请求

response        服务器返回的数据
    response的数据类型是HTTP response
    字节——》字符串
                    解码decode
    字符串——》字节
                    编码Encode
    read()                字节形式读取二进制
    reafline()            读取一行
    readlines()          一行一行读取 直至结束
    getcode()            获取状态码
    ge'turl()                获取url
    getheaders()         获取headers
    
urllib.request.urlretrieve()
    请求网页
    请求图片
    请求视频
```

```python
# urllib基本使用-获取百度页面源码
import urllib.request

# 1. 定义一个url, 就是要访问的地址
url = "http://www.baidu.com"

# 2. 模拟浏览器向服务器发送请求并接收响应
response = urllib.request.urlopen(url)

# 3. 获取响应页面中的源码
# read() 返回的是字节形式的二进制数据，需要将二进制的数据转换为字符串，即解码 decode('编码格式')
content = response.read().decode('utf-8')

# 4. 打印结果
print(content)
```

```python
# urllib基本使用 - 一个类型，六个方法
import urllib.request

# 1. 定义一个url, 就是要访问的地址
url = "http://www.baidu.com"

# 2. 模拟浏览器向服务器发送请求并接收响应
response = urllib.request.urlopen(url)

##################一个类型##################
# print(type(response))
# <class 'http.client.HTTPResponse'>

##################六个方法##################
# content = response.read()       # read() 是按照一个字节一个字节的读
# content = response.read(5)      # read(n) 表示返回n个字节
# content = response.readline()   # readline() 只读取一行
# content = response.readlines()  # readlines() 读取所有行
# print(content)

# print(response.getcode())       # 返回状态码， 200 表示返回正常
# print(response.geturl())        # 返回请求的url地址 http://www.baidu.com
# print(response.getheaders())    # 返回请求头
```

```python
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
```

## 2. 请求对象的定制

UA介绍：User Agent中文名为用户代理，简称 UA，它是一个特殊字符串头，使得服务器能够识别客户使用的操作系统 及版本、CPU 类型、浏览器及版本。浏览器内核、浏览器渲染引擎、浏览器语言、浏览器插件等

语法：`request = urllib.request.Request()`

```python
# urllib基本使用 - 请求对象的定制
import urllib.request

url_page = 'https://www.baidu.com'

# 伪造 headers
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}

# 因为 urlopen 方法中不能存储字典，所以 headers 不能直接作为参数传递，需要定制请求对象
# 注意，因为参数顺序的问题 (Request 需要的三个参数 (url, data=None, headers={}), 中间有个data), 所以需要用关键字传参
request = urllib.request.Request(url=url_page, headers=headers)

response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
print(content)
```

## 3. 编解码

- get请求方式：

  - urllib.parse.quote（）

    quote（）方法能够将汉字转换成unicode编码的格式，适用于单个参数

    ```python
    # urllib基本使用 - 编解码
    import urllib.request
    import urllib.parse
    
    url_page = 'https://www.baidu.com/s?wd='
    
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }
    
    search_word = urllib.parse.quote('周杰伦') # quote（）方法能够将汉字转换成unicode编码的格式，适用于单个参数
    url_page = url_page + search_word
    
    request = urllib.request.Request(url=url_page, headers=headers)
    
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    print(content)
    ```

  - get请求方式：urllib.parse.urlencode（）

    urlencode（）方法也可以将汉字转换成unicode编码，适用于多个参数，多个参数需要放到字典里

    ```python
    # urllib基本使用 - 编解码
    import urllib.request
    import urllib.parse
    
    url_page = 'https://www.baidu.com/s?wd='
    
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }
    
    data = {
        'wd' : '周杰伦',
        'sex' : '男'
    }
    
    search_word = urllib.parse.urlencode(data) # urlencode() 方法也可以将汉字转换成unicode编码，适用于多个参数，多个参数需要放到字典里
    url_page = url_page + search_word
    
    request = urllib.request.Request(url=url_page, headers=headers)
    
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    print(content)
    ```

- post请求方式

  ```python
  # urllib基本使用 - 编解码 - post请求之百度翻译
  import urllib.request
  import urllib.parse
  import json
  
  url_page = 'https://fanyi.baidu.com/sug'
  
  headers = {
      'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
  }
  
  data = {
      'kw' : 'spider'
  }
  
  # post 请求的参数必须要进行编码
  data = urllib.parse.urlencode(data).encode('utf-8')
  
  # post的请求参数需要放在请求对象定制的参数中
  request = urllib.request.Request(url=url_page, data=data, headers=headers)
  
  response = urllib.request.urlopen(request)
  content = response.read().decode('utf-8')
  
  # post请求的响应结果是一个json格式的字符串，需要json解析
  obj = json.loads(content)
  print(obj)
  ```

  ```python
  # urllib基本使用 - post请求之百度翻译-详细翻译
  import urllib.request
  import urllib.parse
  import json
  
  url_page = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'
  
  headers = {
      # 'Accept':'*/*',
      # 'Accept-Encoding':'gzip, deflate, br', 这行指定了可接受的编码格式，但是不包含utf-8,先注释起来
      # 'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8',
      # 'Acs-Token':'1675584313980_1675610295753_u30LM1FFW8cEtKgfvq0kzbWSYrfK+bn1XO39/QqGSxpPVAQRSt8w8udSquJYBYCQXxjPJaTgDIMdglGU5eTzzIDIIPL4Uctg8kwqTGAlmhWD1J/hUHLqCB4aF9qx92IkuTiNTbDSGCQNiFo6s3Amvvd5sfiz1BDXFgHIUSxvyuN7POG97O0XFRZAOIDCK3fVJPWuhzgduG7pa/aPx+cvXrYnn5RSjVt3g5/OEQeov6bbYI2kr0lFm9loKTbxEd8VjTeUQjvKgfC5Lx6WNTgvB2KUPdHe4nsPn8+eYpvM+OaLfitUFuGtIzH0aENRprmuWIDBtLjfkxODl4ckg5TWLQ==',
      # 'Connection':'keep-alive',
      # 'Content-Length':'136',
      # 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
      'Cookie':'PSTM=1664362392; BIDUPSID=A55A48D1030935304D33A040AAED67A4; BDUSS=01LbVB4VUNyVlN4ZkE3cGhDd1ZrdE4wLWlyV1p2bnd2azU5dWZHU0tYSDFYMkpqSVFBQUFBJCQAAAAAAAAAAAEAAAAGaGEouN~O78r9AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPXSOmP10jpjZ; BDUSS_BFESS=01LbVB4VUNyVlN4ZkE3cGhDd1ZrdE4wLWlyV1p2bnd2azU5dWZHU0tYSDFYMkpqSVFBQUFBJCQAAAAAAAAAAAEAAAAGaGEouN~O78r9AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPXSOmP10jpjZ; BAIDUID=DFF5C8264956F30AA8C8AC46F1081ED4:SL=0:NR=10:FG=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID_BFESS=DFF5C8264956F30AA8C8AC46F1081ED4:SL=0:NR=10:FG=1; APPGUIDE_10_0_2=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1675608983; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1675608983; PSINO=2; delPer=0; BA_HECTOR=8h212g21058020048l0505la1htvhjq1k; ZFY=NJUQYDXdXWmdrCNv71Wn7nXhPasNbYVvsiRu5R4eG1w:C; H_PS_PSSID=36557_37521_38094_38130_37910_37989_37921_38089_26350_37959_22158_38008_37881; ab_sr=1.0.1_MjUzZmQyYjAwNjQ2ZTZlMzg1ZWFmNjAzMWJlYjAyZTM5YjI0MjU5YjA2YWQzMzQzYzNhZjRjYWUxM2RjOTg4NzI3MTFiNzk4OGVjODVkYTExN2FkMjdjMTNjYzk2ODRmOWU4ZTRjZDYyZWFkYjRlM2UyZDM2MWI0MmM5NWMwODI4YTIyZTcwMzNmM2ZjYTljYzUzODc5OGM0ZjVkNjNhMmNiNGUyMGYzNzA5MjkwOTVlMGFlNjYxYTBmMWY2YWI3',
      # 'Host':'fanyi.baidu.com',
      # 'Origin':'https://fanyi.baidu.com',
      # 'Referer':'https://fanyi.baidu.com/?aldtype=16047',
      # 'sec-ch-ua':'"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
      # 'sec-ch-ua-mobile':'?0',
      # 'sec-ch-ua-platform':'"Windows"',
      # 'Sec-Fetch-Dest':'empty',
      # 'Sec-Fetch-Mode':'cors',
      # 'Sec-Fetch-Site':'same-origin',
      # 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
      # 'X-Requested-With':'XMLHttpRequest'
  }
  
  data = {
      'from': 'en',
      'to': 'zh',
      'query': 'love',
      'transtype':'translang',
      'simple_means_flag': '3',
      'sign': '198772.518981',
      'token': '7bdf5b0ea077daeca078bc7c76e280b0',
      'domain': 'common'
  }
  
  # post 请求的参数必须要进行编码
  data = urllib.parse.urlencode(data).encode('utf-8')
  
  # post的请求参数需要放在请求对象定制的参数中
  request = urllib.request.Request(url=url_page, data=data, headers=headers)
  
  response = urllib.request.urlopen(request)
  content = response.read().decode('utf-8')
  
  # post请求的响应结果是一个json格式的字符串，需要json解析
  obj = json.loads(content)
  print(obj)
  ```

  - post请求方式与get请求方式区别

    get请求方式的参数必须编码，参数是拼接到url后面，编码之后不需要调用encode方法

    post请求方式的参数必须编码，参数是放在请求对象定制的方法中，编码之后需要调用encode方法

## 4. ajax的get请求

```python
# urllib基本使用 - get请求之获取豆瓣电影第一页的数据并保存
import urllib.request

url_page = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100:90&action=&start=0&limit=20'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}

request = urllib.request.Request(url=url_page, headers=headers)

response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')

# 保存数据到本地
# open 方法默认情况下值班表和的是gbk编码，如果要保存中文则需要在open方法中指定 encoding='utf-8'
fp = open('douban.josn', 'w', encoding='utf-8')
fp.write(content)

# 或者用另一种方法保存数据
# with open('douban.json', 'w', encoding='utf-8') as fp:
#     fp.write(content)
```

```python
# urllib基本使用 - get请求之获取豆瓣电影前10页的数据并保存
import urllib.request
import urllib.parse

def create_request(page):
    base_url='https://movie.douban.com/j/chart/top_list?type=5&interval_id=100:90&action=&'
    data = {
        'start':(page-1)*20,
        'limit':20
    }

    data = urllib.parse.urlencode(data)

    url = base_url + data

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }

    request = urllib.request.Request(url=url, headers=headers)

    return request

def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content

def down_load(page, content):
    with open('douban_' + str(page) + '.json', 'w', encoding='utf-8') as fp:
        fp.write(content)

if __name__ == '__main__':
    start_page = int(input("请输入起始的页码: "))
    end_page = int(input("请输入结束的页码: "))

    for page in range(start_page, end_page+1):
        # 每一页都有自己的请求对象定制
        request = create_request(page)
        # 获取响应数据
        content = get_content(request)
        # 保存数据
        down_load(page, content)
```

