# 继承：子类获得了父类的全部属性及功能,但是不能获得父类的私有属性

# class Person(object):
#     def __init__(self,name,sex):
#         self.name = name
#         self.sex = sex
#
#     def print_title(self):
#         if self.sex == "male":
#             print("man")
#         elif self.sex == "female":
#             print("woman")
#
# class Child(Person):         # Child 继承 Person
#     # def __init__(self, name, sex, age): # 子类自定义初始化方法
#     #     self.name = name
#     #     self.sex = sex
#     #     self.age = age
#
#     def __init__(self, name, sex, age):
#         #Person.__init__(self,name,sex) # 使用父类的初始化方法 可用super关键字代替
#         super().__init__(name, sex)
#         self.age = age
#     def print_title(self):   # 当子类和父类都存在相同的 print_title()方法时，子类的 print_title() 覆盖了父类的 print_title()，在代码运行时，会调用子类的 print_title()这样，这就是继承的另一个好处：多态
#         print("子类")
#
#
# May = Child("May","female",18)
# Peter = Person("Peter","male")
#
# print(May.name,May.sex, May.age, Peter.name,Peter.sex)    # 子类继承父类方法及属性
# May.print_title()
# Peter.print_title()

# 多重继承
# python 3新式类，python2 经典类
# 新式类是在创建的时候继承内置object对象
# 新式类的MRO(Method Resolution Order， 方法解析顺序)，采用的是从左到右，广度优先的方式进行查找。
# 比如下面的代码，类A即为新式类，查找顺序为D->B->C->A，因此print D().name()调用的是类C的name方法，将输出字符C

class A(object):
    def name(self):
        return 'A'

class B(A):
    pass

class C(A):
    def name(self):
        return 'C'

class D(B, C):
    pass

d = D()
print(d.name())
print(D.mro()) # 打印类的继承关系