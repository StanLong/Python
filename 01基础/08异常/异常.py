# 异常

# try:
#     a = 1/0
#     print(a)
# except ZeroDivisionError:
#     print("被除数不能为0")

# 万能异常
# try:
#     a = 1/0
#     print(a)
# except Exception as e:
#     print(type(e), e, e.__traceback__.tb_lineno) # 打印异常行号
# <class 'ZeroDivisionError'> division by zero 12

# 异常分支
# try:
#     a = 1/2
#     print(a)
# except Exception as e:
#     print(type(e), e, e.__traceback__.tb_lineno) # 打印异常行号
# else:
#     print('执行成功')

# finally ： 必定执行的代码
# try:
#     a = 1/0
#     print(a)
# except Exception as e:
#     print(type(e), e, e.__traceback__.tb_lineno) # 打印异常行号
# else:
#     print('执行成功')
# finally:
#     print("不管是否发生异常都执行finally")

# raise 主动抛异常
# try:
#     a = 1/0
#     print(a)
# except Exception as e:
#     raise NameError # 主动抛异常


# 自定义异常
# BaseException
# Exception
# class MyException(Exception):
#     def __init__(self, msg):
#         self.msg = msg
# raise MyException('自定义异常信息')

# 断言
assert True # 效果和 if 一样
print('True就执行')
# assert False 会抛出 AssertionError