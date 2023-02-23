# JsonPath解析

jsonpath适用于解析本地文件，不能用于解析服务器响应文件

```
1.jsonpath安装
        pip安装： pip install jsonpath -i https://pypi.douban.com/simple

2.jsonpath使用
	obj=json.load(open('json文件', 'r', encoding='utf‐8'))
	ret = jsonpath.jsonpath(obj, 'jsonpath语法')
```

jsonpath表达式

| JSONPath           | Description                                                  |
| ------------------ | ------------------------------------------------------------ |
| $                  | 表示根元素                                                   |
| @                  | 当前元素                                                     |
| . or []            | 子元素                                                       |
| n/a                | 父元素                                                       |
| ..                 | 递归下降，JSONPath是从E4X借鉴的。                            |
| *                  | 通配符，表示所有的元素                                       |
| n/a                | 属性访问字符                                                 |
| []                 | 子元素操作符                                                 |
| [,]                | 连接操作符在XPath  结果合并其它结点集合。JSONP允许name或者数组索引。 |
| `[start:end:step]` | 数组分割操作从ES4借鉴。                                      |
| ?()                | 条件过滤                                                     |
| ()                 | 脚本表达式，使用在脚本引擎下面。                             |
| n/a                | Xpath分组                                                    |

```python
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
```

