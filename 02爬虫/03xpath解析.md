# 解析

# 一、xpath

> xpath是一门在XML文档中查找信息的语言。xpath可用来在XML文档中对元素和属性进行遍历。

**xpath使用**

- 在浏览器中配置xpath插件 

  [xpath的下载与安装](https://blog.csdn.net/qq_43576837/article/details/108410989) 

1. 安装lxml库 `pip install lxml`

2. 导入lxml.etree `from lxml import etree`

3. etree.parse() 解析本地文件 `html_tree=etree.parse('XX.html')`

4. etree.HTML() 服务器响应文件`html_tree = etree.HTML(response.read().decode('utf‐8')`

5. html_tree.xpath(xpath路径)