# 解析

# 一、xpath

> xpath是一门在XML文档中查找信息的语言。xpath可用来在XML文档中对元素和属性进行遍历。

**xpath使用**

- 在浏览器中配置xpath插件 

  [xpath的下载与安装](https://blog.csdn.net/qq_43576837/article/details/108410989) 
  
- 安装lxml库

  安装lxml库 `pip install lxml`

  ```powershell
  # 进入到python的安装目录，在Scripts 目录下使用豆瓣源安装
  D:\Program Files\Python\Python37\Scripts>pip install lxml -i https://pypi.douban.com/simple
  Looking in indexes: https://pypi.douban.com/simple
  Collecting lxml
    Downloading https://pypi.doubanio.com/packages/20/5b/caca461e172d696b151e50a182c6111d192175571e34f483a477122c5d79/lxml-4.9.2-cp37-cp37m-win_amd64.whl (3.8MB)
       |████████████████████████████████| 3.9MB 6.4MB/s
  Installing collected packages: lxml
  Successfully installed lxml-4.9.2
  ```

- xpath基本语法

  ```
  1. 路径查询
  	// : 查询所有子孙节点，不考虑路径关系
  	/  : 查找直接子节点
  2. 谓词查询
      //div[@id]
      //div[@id="maincontent"]
  3. 属性查询
  	//@class
  4. 模糊查询
  	//div[contains(@id, "he")]
  	//div[starts-with(@id, "he")]
  5. 内容查询
  	//div/h1/text()
  6. 逻辑运算
  	//div[@id="head" and @class="s_down"]
  	//title | // price
  ```

## 1. 解析本地文件

```python
# xpath的基本使用
from lxml import etree

# xpath 解析本地文件
tree = etree.parse('03xpath解析本地文件.html') # 解析本地文件

# 查找 ul 下的 li
# li_list = tree.xpath('//body/ul/li')
# print(len(li_list))

# 查找所有有id属性的li标签
# li_list = tree.xpath("//ul/li[@id]")
# print(li_list)
# print(len(li_list))

# 查找所有有id属性的li标签中的内容
# text() 获取标签中的内容
# li_list = tree.xpath("//ul/li[@id]/text()")
# print(li_list)

# 找到id为1的li标签
# li_list = tree.xpath('//ul/li[@id="1"]/text()')
# print(li_list)

# 查找到id为1的li标签的class的属性值
# li_list = tree.xpath('//ul/li[@id="1"]/@class')
# print(li_list)

# 查询id中包含i的li标签
#li_list = tree.xpath('//ul/li[contains(@id, "i")]/text()')
#print(li_list)

# 查询id的值以i开头的li标签
# li_list = tree.xpath('//ul/li[starts-with(@id, "i")]/text()')
# print(li_list)

# 查询id为1 和 class 为 c1 的 li 标签
# li_list = tree.xpath('//ul/li[@id="1" and @class="c1"]/text()')
# print(li_list)

li_list = tree.xpath('//ul/li[@id="1"]/text() | //ul/li[@id="2"]/text()')
print(li_list)
```

## 2. 解析网页源码

```python
# xpath的基本使用-解析网页源码-获取“百度一下”四个字
from lxml import etree
import urllib.request
url="http://www.baidu.com"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}

# 请求对象的定制
request = urllib.request.Request(url=url, headers= headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')

tree = etree.HTML(content)  # 解析网页源码
result = tree.xpath('//input[@id="su"]/@value')
print(result)
```

```python
# 使用xpath解析站长之家下载前十页的图片

import urllib.request
from lxml import etree

def create_request(page):
    if page == 1:
        url = 'https://sc.chinaz.com/tupian/qinglvtupian.html'
    else:
        url = 'https://sc.chinaz.com/tupian/qinglvtupian_' + str(page) + '.html'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    }

    request = urllib.request.Request(url = url, headers= headers)
    return request

def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content

def down_load(content):
    tree = etree.HTML(content)
    # 一般涉及到图片的网站都会涉及懒加载
    # 注意这里会遇到一个问题，参考 https://blog.csdn.net/m0_57753629/article/details/128638474
    name_list = tree.xpath('//div[@class="item"]/img/@alt')
    src_list = tree.xpath('//div[@class="item"]/img/@data-original')

    for i in range(len(name_list)):
        name = name_list[i]
        src = src_list[i]
        url = 'https:' + src
        print(name, url)
        urllib.request.urlretrieve(url=url, filename='./tupian/' + name + '.jpg')

if __name__ == '__main__':
    start_page = int(input('请输入起始页码'))
    end_page = int(input('请输入结束页码'))

    for page in range(start_page, end_page+1):
        # 请求对象的定制
        request = create_request(page)
        # 获取网页源码
        content = get_content(request)
        # 下载图片
        down_load(content)
```

