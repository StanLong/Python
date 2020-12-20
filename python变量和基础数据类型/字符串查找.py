s='年轻人，想要做成大事，就要学会等待'

# 判断是否以指定字符开头
# print(s.startswith('年轻人')) # True
# print(s.startswith('\('))    # False

# 判断是否以指定字符结尾
# print(s.endswith('等待')) # True
# print(s.endswith('\)')) # False

# 统计指定字符出现的次数
# print(s.count('要')) # 2

# 查找指定字符, 返回查找字符在字符串中的位置
# print(s.find('大事'))   # 8
# print(s.find('刘伯温')) # -1

# 切片查找字符
# print(s.find('大事', 8)) # 8

# 返回查找字符在指定字符串中的位置，和find的区别在于，如果查找字符串的不存在，则直接报错
# print(s.index('想要')) # 4