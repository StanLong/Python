# urllib基本使用 - post请求之百度翻译-详细翻译
import urllib.request
import urllib.parse
import json

url_page = 'https://fanyi.baidu.com/sug'

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