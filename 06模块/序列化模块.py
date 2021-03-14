# 序列号
# 字典、列表、数字、对象 序列号成字符串
# 字符串 反序列化 字典、列表、数字、对象

# 三种序列化工具
# json
    # 支持的数据类型有限，但是可以跨语言
    # key必须是字符串类型，如果是数字，dumps会强行转成字符串类型，字符串类型要用""
    # 支持元组作为value，但是不支持元组作为key
    # set 不能被 dump/dumps
    # 操作json文件的时候用dump/load
    # dumps是将dict转化成str格式，loads是将str转化成dict格式。
    # dump和load也是类似的功能，只是与文件操作结合起来了
# pickle
    # 可以支持所有数据类型，但是不能跨语言
    # 不会修改数据
    # 序列化的数据是二进制编码，不好阅读
    # dump/dunmps的结果是byte， dump用的f文件句柄需要以wb的模式打开，load加载文件需要用rb模式打开
    # 对于对象序列化，需要对象对应的类再内存中

# json
import json

# dic = {'k':'v'}
# str_dic = json.dumps(dic) # 字典序列化成字符串
# print(str_dic, type(str_dic))
# {"k": "v"} <class 'str'>

# dic_str = json.loads(str_dic)
# print(dic_str, type(dic_str)) # 字符串反序列化成字典
# {'k': 'v'} <class 'dict'>

# 中文格式
# # 表示不用 ascii 码存储
# sort_keys=True, indent=2, separators=(',',':') 格式化展示json
# dic={"country":"中国"}
# dic_str = json.dumps(dic, ensure_ascii=False, sort_keys=True, indent=2, separators=(',',':'))
# print(dic_str)
# {
#   "country":"中国"
# }

# pickle
# import pickle
# dic = {1:(1,2,3), ('a','b'):'c'}
# pic_dic = pickle.dumps(dic)
# print(pic_dic)
#b'\x80\x03}q\x00(K\x01K\x01K\x02K\x03\x87q\x01X\x01\x00\x00\x00aq\x02X\x01\x00\x00\x00bq\x03\x86q\x04X\x01\x00\x00\x00cq\x05u.'
# dic_pic = pickle.loads(pic_dic)
# print(dic_pic)
# {1: (1, 2, 3), ('a', 'b'): 'c'}