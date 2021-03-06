#hashlib模块
# 摘要算法， 能够把一个字符串数据类型的变量转换成一个定长的密文字符串，字符串里的每一个字符都是十六进制数字
# 对于同一个字符串，不关这个字符串有多长，
# 只要是相同的，无论再任何环境下，执行多少次，再任何语言中
# 得到的结果永远是相同的

# 只要是不相同的字符串，得到的结果一定不一样

import hashlib
# md5的结果会得到一个32位的字符串，每个字符串都是十六进制
# s = 'abc'
# md5_obj = hashlib.md5()
# md5_obj.update(s.encode('utf-8'))
# res = md5_obj.hexdigest()
# print(res, len(res), type(res))
# 900150983cd24fb0d6963f7d28e17f72 32 <class 'str'>

# md5加盐
# s = 'abc'
# md5_obj = hashlib.md5('任意的字符串作为盐'.encode('utf-8')) # 加盐
# md5_obj.update(s.encode('utf-8'))
# res = md5_obj.hexdigest()
# print(res, len(res), type(res))
# 0417c7fcf8ee0b3e6d82d6792c594040 32 <class 'str'>

# sha1
# s = 'abc'
# md5_obj = hashlib.sha1()
# md5_obj.update(s.encode('utf-8'))
# res = md5_obj.hexdigest()
# print(res, len(res), type(res))
# a9993e364706816aba3e25717850c26c9cd0d89d 40 <class 'str'>
