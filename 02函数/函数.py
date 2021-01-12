# 函数入门， 执行顺序 2 -> 4 -> 3
# def fun():
#     print('贵出如粪土，贱取如珠玉')
# fun()

# 函数返回值, 执行顺序 7 -> 10 -> 8 -> 9
# def fun():
#     print('贵出如粪土，贱取如珠玉')
#     return "年轻人，想要做成大事，一定要学会等待"
#     return "沈万三", "朱元璋"
# ret = fun()
# print(ret)
# 如果函数种不写 return ， 默认返回nul
# 如果有多个返回值，变量打印的数据类型是一个元组

# 函数传参
# 位置参数
# def fun(name, words):
#     print("%s说: %s" %(name, words))
# fun("南海财神", "无息币，勿完物")

# 关键字参数
# def fun(name, words):
#     print("%s说: %s" % (name, words))
# fun(name='南海财神', words = '无息币，勿完物')

# 默认值参数
# def fun(name, words, dynasty='明朝人'):
#     print("%s, %s他说: %s" % (name, dynasty, words))
# fun("南海财神", "无息币，勿完物")
# fun("岳飞", "满江红", "宋朝人")

# 动态参数
# * 位置参数  ** 关键字参数
# def fun(*name):
#     print(name)
# fun('沈万三', '东山钱王', '湖西银童', '漠北富婆', '南海财神')
# ('沈万三', '东山钱王', '湖西银童', '漠北富婆', '南海财神')
# 动态位置参数接收的是一个元组类型的参数

# 动态接收关键字参数
# def fun(**name):
#     print(name)
# fun(east='东山钱王', south='南海财神', west = '湖西银童', north = '漠北富婆')
# {'east': '东山钱王', 'south': '南海财神', 'west': '湖西银童', 'north': '漠北富婆'}
# 动态关键字参数接收的是一个字典类型的参数

#print(globals())  # 获取全局作用域（内置，全局）中的所有名字
#print(locals())  # 查看当前作用域中所有的名字

# a = 10
# def func():
#     # a = 20 # 在自己的作用域中使用的a。是全新的变量a
#     global a # 使用全局变量（51行）中的a
#     a = a + 10
#     print(a)
# func()
# print(a)


def func1():
    a = 10
    def func2():
        nonlocal a # 找局部作用域中最近的那个变量， 这里是引入第62行的a
        a = 20
        print(a)
    func2()
    print(a)
func1()