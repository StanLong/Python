print("这是一个自定义模块")
name = "自定义模块"
def func():
    print("这是一个自定义方法 func")


# 所有不在函数和类中封装的内容都应该写在 if __name__ == '__main__': 下
if __name__ == '__main__': # 判断是否时当前模块，以下内容只在当前模块执行，当该模块被引用时不执行
    print(__name__, type(__name__))
