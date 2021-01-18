# 闭包就是内层函数对外层函数（非全局）的变量的引用叫闭包。变量写在全局使不安全的，所以使用闭包，防止其他程序改变变量
# 闭包可以让一个局部变量常驻内存

# def func():
#     name="沈万三"
#     def inner():
#         print(name) # 在内层函数调用了外层函数的变量（name）,这个就叫闭包
#     # print(inner.__closure__) 打印结果不为空说明inner是个闭包
#     return inner
# ret = func()
# ret()


# 迭代器：节省内存，惰性机制，不能反复只能向下执行
# 可迭代对象 str, list, tuple, set, f(文件句柄) dict
# 以上数据类型中都有一个函数 __iter__()
# dir() 可以查看一个对象或者数据类型中包含了哪些东西
lst = ['沈万三', '刘伯温', '朱元璋']
#print(dir(lst))
#print('__iter__' in dir(lst)) # True
# it = lst.__iter__()
# print(it.__next__()) # 使用 __next__ 从迭代器里往外拿元素
# # 沈万三
# print(it.__next__()) # 使用 __next__ 从迭代器里往外拿元素
# # 刘伯温
# print(it.__next__()) # 使用 __next__ 从迭代器里往外拿元素
# print(it.__next__()) # 使用 __next__ 从迭代器里往外拿元素 # 迭代到最后一个元素在继续迭代的话就报错了 StopIteration

from collections.abc import Iterable
from collections.abc import Iterator

print(isinstance(lst, Iterable)) # True 可迭代的
print(isinstance(lst, Iterator)) # False # 不是迭代器