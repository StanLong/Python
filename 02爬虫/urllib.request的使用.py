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

