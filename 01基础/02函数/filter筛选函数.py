# filter 筛选函数
# 语法
# filter(function, Iterable)
# function 筛选函数
# Iterable 可迭代对象
lst = [1,2,3,4,5,6]
ll = filter(lambda i:i%2==1, lst)
print(ll) # filter 函数返回一个迭代器
# <filter object at 0x000002DB3AAFB4C8>
print(list(ll))
# [1, 3, 5]
