# 序列号
# 字典、列表、数字、对象 序列号成字符串
# 字符串 反序列化 字典、列表、数字、对象

# 三种序列化工具
# json
    # 支持的数据类型有限，但是可以跨语言
# pickle
    # 可以支持所有数据类型，但是不能跨语言
# shelve

# json
import json

dic = {'k':'v'}
str_dic = json.dumps(dic) # 字典序列化成字符串
print(str_dic, type(str_dic))
# {"k": "v"} <class 'str'>

dic_str = json.loads(str_dic)
print(dic_str, type(dic_str)) # 字符串反序列化成字典
# {'k': 'v'} <class 'dict'>