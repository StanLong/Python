# import urllib.request

# url = 'http://www.baidu.com'
# response = urllib.request.urlopen(url=url) # 返回一个对象
# 对象方法
# read() 获取响应的内容， 内容是字节类型
# geturl() 获得请求的链接
# getheaders() 获得响应头信息
# getcode()    获得响应状态码
# readlines()   按行读取，返回列表

# print(response.read().decode('utf-8'))
# print(response.geturl())
# print(response.getheaders())
# print(response.getcode())
# print(response.readlines())

####################################################################################################
# 下载图片
# image_url = 'http://5b0988e595225.cdn.sohucs.com/images/20180107/61e1f23fe19f40b7b2c370e6218fdcb9.jpeg'

# 方式一
# response = urllib.request.urlopen(url=image_url)
# with open('meizi.jpeg', 'wb') as f_w:
#     f_w.write(response.read())

# 方式二
# urllib.request.urlretrieve(image_url, 'meizi2.jpeg')

####################################################################################################

import urllib.parse
# url 只能由数字、字母、下划线组成， 如果出现了其他的字符，就要对其进行编码
# url = 'http://wwww.baidu.com/index.html?name=沈万三&pwd=123456'
# ret = urllib.parse.quote(url) # 对url进行编码
# print(ret) # http%3A//wwww.baidu.com/index.html%3Fname%3D%E6%B2%88%E4%B8%87%E4%B8%89%26pwd%3D123456

# ret = urllib.parse.unquote('http%3A//wwww.baidu.com/index.html%3Fname%3D%E6%B2%88%E4%B8%87%E4%B8%89%26pwd%3D123456') # 对url解码
# http://wwww.baidu.com/index.html?name=沈万三&pwd=123456
# print(ret)

# data = {
#     "name":"沈万三",
#     "dynasty":"ming",
#     "job": "trader"
# }
# query_string = urllib.parse.urlencode(data) # 格式化查询参数， 入参是一个字典
# print(query_string) # name=%E6%B2%88%E4%B8%87%E4%B8%89&dynasty=ming&job=trader