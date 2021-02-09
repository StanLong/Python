# 多态： 多态性是指在不考虑实例类型的情况下使用实例，多态性分为静态多态性和动态多态性
class Animals(object):
    def talk(self):
        pass

class People(Animals):
    def talk(self):
        print('People is talking')
    def eat(self):
        print('People can eat')


class Cat(Animals):
    def talk(self):
        print('Cat is miaomiao')

class Dog(Animals):
    def talk(self):
        print('Dog is wangwang')

cat1 = Cat()
dog1 = Dog()
peo1 = People()
# peo、dog、pig都是动物,只要是动物肯定有talk方法
# 于是我们可以不用考虑它们三者的具体是什么类型,而直接使用
peo1.talk()
dog1.talk()
peo1.talk()

# 定义一个统一的接口来访问
def func(obj):
    obj.talk()

func(cat1)

# 抽象类（接口类）: 所有继承抽象类或者接口类的方法必须重写父类中 @abc.abstractmethod 标记的方法
# import abc
# class Animals(metaclass=abc.ABCMeta):
#     @abc.abstractmethod
#     def talk(self):
#         pass
#
# class People(Animals): # 不然会报错 TypeError: Can't instantiate abstract class People with abstract methods talk
#     def eat(self):
#         print('People can eat')
#
# class Cat(Animals):
#     def talk(self):
#         print('Cat is miaomiao')
#
# class Dog(Animals):
#     def talk(self):
#         print('Dog is wangwang')
#
# cat1 = Cat()
# dog1 = Dog()
# peo1 = People()
# peo1.talk()
# dog1.talk()
# peo1.talk()
#
# # 定义一个统一的接口来访问
# def func(obj):
#     obj.talk()
#
# func(cat1)