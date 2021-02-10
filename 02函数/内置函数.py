# eval ： 执行字符串类型的代码，并返回最终结果
# s = input('输入a+b:')
# print(eval(s)) # eval 可以动态的执行代码，代码必须有返回值

# exec: 执行字符串类型的代码，不返回任何内容
# s = "25*4"
# a = exec(s) # exec 不返回任何内容
# print(a)
# None
# exec 执行函数
# exec("""
# def func():
#     print("贵出如粪土，贱取如珠玉")
#
# func()
# """)

# compile 将字符串代码编译，代码对象能够通过exec来执行或者通过eval进行求值
# 参数说明
# 1. resource 要执行的代码，动态代码片段
# 2. 文件名，代码存放的文件名，当传入了第一个参数的时候，这个参数给空就可以了
# 3. 模式 取值有三个
#   1. exec: 一般放一些流程语句的时候
#   2. eval：resource 只存放一个求值表达式
#   3. single： resource 存放的代码有交互的时候，mode应为single
# code1 = "for i in range(10):print(i)"
# com = compile(code1, "", mode="exec") # compile 只是编译，不会执行代码
# exec(com)

# code2 = "5+6"
# com = compile(code2, "", mode="eval")
# print(eval(com))

# code3 = "name=input('请输入沈万三的身份：')"
# com = compile(code3, "", mode="single")
# exec(code3)
# print(name)

# repr 原样输出
# name = "沈万三\n明朝人"
# print(repr(name))
# '沈万三\n明朝人'

# ord 返回字符在编码表中的码位
# print(ord('a'))
# 97

# chr 返回码位对应的字符
# print(chr(97))
# a

# format 与具体数据有关，用于计算各种小数，精算等
# print(format(10, 'b')) # 二进制
# 1010

# divmod 求商和余数
# print(divmod(7,3))

# pow(a,b,c) 求a的b次幂，如果有三个参数，则求完次幂后对第三个数取余
# print(pow(2,2,3))

# isinstance()函数
# 判断一个对象是否是一个已知的类型，返回布尔值。类似 type()
# 但是：
# type() 不会认为子类是一种父类类型，不考虑继承关系。  　　
# isinstance() 会认为子类是一种父类类型，考虑继承关系。  　　
# 如果要判断两个类型是否相同推荐使用 isinstance()
# class A:
#     pass
#
# class B(A):
#     pass
#
# print(isinstance(A(),A))    # True
# print( type(A()) == A )     # True
#
# print(isinstance(B(),A))    # True
# print( type(B()) == A )     # False   --type()不考虑继承关系

# issubclass() 函数
# 用于判断参数class是否是类型参数classinfo的子类，是则返回True，否则返回False
# class A:
#     pass
# class B(A):     # B继承了A，即B是A的子类
#     pass
#
# print(issubclass(A,B))    # 判断 A 是 B 的子类？
# # False
# print(issubclass(B,A))    # 判断 B 是 A 的子类？
# # True