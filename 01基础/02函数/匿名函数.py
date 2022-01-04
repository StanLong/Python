# lambda 匿名函数
# 代码格式
# 函数名 = lambda 参数 : 函数体（直接return的内容）
a = lambda x : x*x
print(a)
# <function <lambda> at 0x000002B013BF03A8>
print(a(6))
# 36

b = lambda x,y : x+y
print(b(1,4))
# 5