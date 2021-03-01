# re 模块

# print('a\nb')
# print(r'a\nb') # r 表示取消转义

import  re

# re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none
# str = "abcdabcdwww"
# print(re.match("abc", str))
# <re.Match object; span=(0, 3), match='abc'>
# print(re.match("abc", str).group())
# abc
# print(re.match("abc", str).groups())
# print(re.match("www", str)) # www 不在字符串开头， 返回None

# re.search 扫描整个字符串并返回第一个成功的匹配。
str = "abcdabcdwww"
# print(re.search("abc", str))
# <re.Match object; span=(0, 3), match='abc'> # 只返回了第一个匹配到的abc
# print(re.search("abc", str).group())
# abc
# print(re.search("www", str))
# <re.Match object; span=(8, 11), match='www'>
# print(re.search("www", str).group())
# www
# print(re.search("(abc)(dw)", str)) 如果遇到分组， group(n) 打印第n个分组的内容, 这种方法也叫分组的下标索引
# <re.Match object; span=(4, 9), match='abcdw'>
# print(re.search("(abc)(dw)", str).group(1))
# abc
# print(re.search("(abc)(dw)", str).group(2))
# dw


# re.search 的匹配范围要比 re.match 大

# re.sub 用于替换字符串中的匹配项
# str = "abcdabcdwww"
# print(re.sub("www", "com", str)) # 把www替换成com
# abcdabcdcom
# print(re.sub("abc","xyz", str)) #  把匹配到的所有abc替换成xyz
# xyzdxyzdwww

# re.findall 在字符串中找到正则表达式所匹配的所有子串，并返回一个列表,
# 如果遇到分组，会优先显示分组中的内容
# 如果没有找到匹配的，则返回空列表
# str = "abcdabcdwww"
# print(re.findall("www", str))
# ['www']
# print(re.findall("(www)", str))
# ['www']
# print(re.findall("bcd(www)", str))
# ['www']
# print(re.findall("bcd(?:www)", str)) # 取消分组优先
# ['bcdwww']


# re.finditer 和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回
# str = "abcdabcdwww"
# print(re.finditer("abc", str))
# <callable_iterator object at 0x000001E7FF5AF388>
# print(re.finditer("abc", str).__next__())
# <re.Match object; span=(0, 3), match='abc'>
# print(re.finditer("abc", str).__next__().group())
# abc

# re.split 方法按照能够匹配的子串将字符串分割后返回列表，它的使用形式如下
# 如果遇到分组，会保留分组内被切掉的内容，在列表中显示出来
# str = "abcdabcdwww"
# print(re.split("abc", str))
# ['', 'd', 'dwww']
# print(re.split("(abc)", str))
# ['', 'abc', 'd', 'abc', 'dwww']

# re.compile 用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，给re的其他函数使用
# pattern = re.compile("abc")
# str = "abcdabcdwww"
# print(pattern.match(str))
# <re.Match object; span=(0, 3), match='abc'>
# print(pattern.match(str).group())
# abc

# 正则表达式修饰符 - 可选标志
# re.I	使匹配对大小写不敏感
# re.L	做本地化识别（locale-aware）匹配
# re.M	多行匹配，影响 ^ 和 $
# re.S	使 . 匹配包括换行在内的所有字符
# re.U	根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
# re.X	该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。


# 分组别名
# (?P<name>正则表达式) 表示给分组起名字
# (?P=name) 表示使用这个分组，这里匹配到的内容应该和分组中的内容完全相同
# str="<a>wahaha</b>"
# print(re.search(r'<(?P<tag>\w+)>(?P<c>\w+)</(\w+)>', str))
# <re.Match object; span=(0, 13), match='<a>wahaha</b>'>
# print(re.search(r'<(?P<tag>\w+)>(?P<c>\w+)</(\w+)>', str).group("tag"))
# a
# print(re.search(r'<(?P<tag>\w+)>(?P<c>\w+)</(\w+)>', str).group("c"))
# wahaha