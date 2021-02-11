# 内置方法
# __call__
# class A:
#     def __call__(self, *args, **kwargs):
#         print("执行__call__方法")
#
# A()() # 相当于调用了 __call__ 方法
# a = A()
# a()    # 相当于调用了 __call__ 方法


# __new__ 构造方法
class Single:
    def __new__(cls, *args, **kwargs):
        print('执行了__new__方法')
        return super().__new__(cls)
    def __init__(self):
        print('执行了__init__ 方法')

obj = Single()
# 实例化 Single 后，先执行了 __new__ 方法， 后执行了 __init__ 方法
# __new__在实例化对象之后，__init__ 之前执行


# __len__
class Mylist:
    def __init__(self):
        self.lst = [1,2,3]
    def __len__(self):
        print("执行 __len__ 函数")
        return len(self.lst)
mylist = Mylist()
print(len(mylist)) # 打印对象的长度，相当于执行了类中的 __len__ 方法

# __str__
class Student:
    def __str__(self):
        return '%s %d %s'%(self.name, self.age, self.job)
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job
student = Student("沈万三", 30, "商人")
print(student.name, student.age, student.job) # 打印一个对象的全部属性，如果不想这么麻烦可以实现 __str__ 方法
print(student) # 实现 __str__ 后再打印对象，会直接打印出对象的全部属性

# __repr__
# __repr__ 是 __str__ 的备用方法，如果有__str__方法，那么print('%s' %str) 都先执行__str__的方法
a = '123'
print(a) # 123
print(repr(a)) # '123'

class A:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return '*%s*' %self.name
    def __repr__(self):
        return self.name
a = A('StanLong')
print(a) # 有 __str__ 则先打印 *StanLong*，否则打印 StanLong

