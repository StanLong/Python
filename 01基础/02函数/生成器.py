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

# send() 函数
# def func():
#     print("沈万三")
#     a = yield "商人"
#     print(a)
#     print("朱元璋")
#     b = yield "皇帝"
#     print("东山钱王")
#     c = yield "财神"
# g = func()
# print(g.__next__())
# print(g.send(1))
# print(g.__next__())
# print()
# __next__() 可以让生成器向下执行一次
# send() 也可以让生成器向下执行一次,给上一个yield传一个值，本例中给a传了一个1。 生成器第一个位置不能用send(),最后一个也不能用

# 列表推导式
# 语法 [最终结果 for 变量 in 可迭代对象]
# lst = ['四大财神之%s' %s for s in('东山钱王', '西湖银童', '漠北富婆', '南海财神')]
# print(lst)

# 生成器表达式
# gen = (s for s in ('东山钱王', '西湖银童', '漠北富婆', '南海财神'))
# print(gen)
# <generator object <genexpr> at 0x000001C52BBD0F48>
# print(gen.__next__())
# 东山钱王

# 字典推导式
# dic = {"沈万三":"商人", "朱元璋":"皇帝", "刘伯温":"老师"}\

# 把字典中的key : value 互换
# new_dic = {dic[key]:key for key in dic}
# print(new_dic)

# 集合推导式
lst = ['东山钱王', '西湖银童', '漠北富婆', '南海财神']
s = {i for i in lst}
print(s)