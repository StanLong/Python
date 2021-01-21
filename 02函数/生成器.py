# 生成器的本质就是迭代器

# 生成器函数
# def func():
#     print("沈万三")
#     yield "明朝首富" # yield 表示当前函数使生成器函数
#     print("朱元璋")
#     yield "明朝开国皇帝"
# print(func())
# <generator object func at 0x0000028B84B00EC8>
# g = func() # 通过函数func来创建一个生成器
# print(g.__next__())
# 沈万三
# 明朝首富
# print(g.__next__())
# 沈万三
# 明朝首富
# 朱元璋
# 明朝开国皇帝

# return 直接返回结果，结束函数调用
# yield 返回结果，可以让函数分段调用