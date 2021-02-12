# 析构方法
# 对象被销毁时执行的操作,当对象在内存中被释放时，自动触发执行

# 垃圾回收机制
class A:
    def __del__(self):
        print('执行了删除方法') # 执行删除对象 del a的操作，会自动出发这个方法

a = A()
# del a
print(a) # 任执行了 __del__ 方法，说明创建的所有变量，都会在结束时由python解释器回收


