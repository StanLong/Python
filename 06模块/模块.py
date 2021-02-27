# 模块是具有相同类别的一组功能。在Python中，每个Python文件都可以作为一个模块，模块的名字就是文件的名字
# https://cn.ac101.click/
# import 模块名
    # import 模块名 相当于执行了这个模块所在的py文件
# 一个模块不会被重复导入


# 使用自定义模块
# import my_module
# my_module.func()
# print(my_module.name)
# 这是一个自定义模块
# 这是一个自定义方法 func
# 自定义模块

# 模块的重命名
# import my_module as m
# m.func()
# print(m.name)

# import sys
# print(sys.modules['__main__']) # 打印模块所在地址
# <module '__main__' from 'D:/StanLong/git_repository/Python/06模块/模块.py'>

# import importlib
# import my_module
# import time
# my_module.func()
# time.sleep(10)
# # 表示重新加载, reload 可以强制程序再重新导入这个模块一次，非常不推荐使用， 因为import之后，再修改这个模块，程序感知不到
# importlib.reload(my_module)
# my_module.func()

# 在模块导入中，不要产生循环引用的问题

# 导入包相当于导入这边包下面的 __init__.py 文件
# import my_package

# 可以编写 __init__.py 文件， 提前导入一些模块
# 从包中导入模块，要注意这个包所在的目录是否在sys.path
# from my_package import my_module
# my_module.func()

# 使用了相对导入的模块只能被当作模块执行，不能被当作包执行

# 将包名加入到 sys.pth 里
# import sys
# ret = __file__.split('/') # __file__ 文件的绝对路径
# base_path = '/'.join(ret[:-2])
# sys.path.append(base_path)


print(__file__)