# xpath的基本使用
from lxml import etree

# xpath 解析本地文件
tree = etree.parse('03xpath解析本地文件.html')

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