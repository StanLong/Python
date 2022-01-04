# map 映射函数
# 语法: map(function, iterable) 可以对迭代对象中的每一个元素进行映射，分别去执行function

# lst = [1,2,3,4,5,6]
# ll = map(lambda x:x*x, lst)
# print(ll) # map 返回一个迭代器对象
# # <map object at 0x000002185DA6B4C8>
# print(list(ll))

lst1 = [1,3,5]
lst2 = [2,4,6]
print(list(map(lambda x,y:x+y, lst1, lst2))) # 如果有多个参数，参数列表要一一对应
# [3, 7, 11]