import json
import jsonpath

# 导入json文件
obj = json.load(open('04JsonPath解析.json', 'r', encoding='utf-8'))


# 书店所有书的作者
# auth_list = jsonpath.jsonpath(obj, '$.store.book[*].author')

# 所有的作者
# auth_list = jsonpath.jsonpath(obj, '$..author')

# store 下面所有的元素
# tag_list = jsonpath.jsonpath(obj, '$.store.*')

#store 里面所有的 price
# price_list = jsonpath.jsonpath(obj, '$.store..price')

# 第三本书
# book = jsonpath.jsonpath(obj, '$..book[2]')

# 最后一本书
# book = jsonpath.jsonpath(obj, '$..book[(@.length-1)]')

# 前两本书
# book_list = jsonpath.jsonpath(obj, '$..book[0,1]')
# 或者用切片的方式
# book_list = jsonpath.jsonpath(obj, '$..book[:2]')

# 过滤出包含所有版本号的书
# book_list = jsonpath.jsonpath(obj, '$..book[?(@.isbn)]')

# 超过10块钱的书
book_list = jsonpath.jsonpath(obj, '$..book[?(@.price > 10)]')
print(book_list)






