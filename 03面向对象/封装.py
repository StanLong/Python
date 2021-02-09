#封装(实际封装python中的封装只是一个约定)
# 第一层面的封装：类就好像一个袋子，这就是一种封装
# 第一阶段：
# 如果我们要定义学生jack如何定义？
# name = 'jack'
# age = 17
# sex = '男'
# 这三个变量可以用来形容jack这个人（当然你也可以使用字典，列表去描述).但是我们用三个变量去形容这个人，有什么弊端？
# 	弊端：太零散，如果学生太多，需要有很多变量去描述
# 为了解决这个问题，因此才有了类。
# 第二阶段：
# class Student(object):
#
#     def __init__(self,name,age,sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
# one = Student('jack',17,'男') # 这里的one就相当于一个学生jack，所有的属性都封装到了one变量中。这里的Student类，相当于一个模板。只要给定它name，age，sex，它就能创建出一个学生对象。
# two = Student('aaa',16,'男')
# three = Student('bbb',15,'女')
# four = Student('ccc',14,'男')
# five = Student('ddd',13,'女')
# print(f'姓名:{one.name}   年龄:{one.age}    性别:{one.sex}')

# 第二层面的封装：类中定义私有的,只有类内部使用,外部无法访问(比如_(杠) __(杠杠) )
# 第一阶段：
# class Student(object):
#
#     def __init__(self,name,age,sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
# one = Student('plf',18,'男')
# one.name = 'who'
# one.age = -28
# one.sex = '人妖'
# print(f'姓名:{one.name}   年龄:{one.age}    性别:{one.sex}')
# 问题：我们在外部能随意访问到对象one的属性，并且随意修改，这样数据是不安全的，因为我们需要将属性隐藏起来。
# 第二阶段：
# class Student(object):
#
#     def __init__(self,name,age,sex):
#         self.__name = name
#         self.__age = age
#         self.__sex = sex
# one = Student('plf',18,'男')
#
# print(one._Student__name)
# print(one._Student__age)
# print(one._Student__sex)
#
# one._Student__age = 20
# print(one._Student__age)
#
# print(one.__name)       # 报错，无该属性
# print(one.name)         # 报错，无该属性
#此时发现，我们虽然不能使用one.name或者one.__name访问到该属性。但是我们可使用one._Student__age访问到对象的age属性并且能修改。
# 说明python在设置私有属性的时候，只是把属性的名字换成了其他的名字
# 总结：
#​类中以_或者__的属性，都是私有属性，禁止外部调用。虽然我们可以通过特殊的手段获取到，并且赋值，但是最好不要这么做（约定俗成）
# 问题：现在我将name，age，sex设置为私有属性，但是我又想让他们通过我指定的接口去访问或者修改我的属性，应该如何实现了
# 第三阶段：
# class Student(object):
#     def __init__(self,name,age,sex):
#         self.__name = name
#         self.__age = age
#         self.__sex = sex
#     def get_name(self):
#         return self.__name
#     def set_name(self,name):
#         if len(name) > 1 :
#             self.__name = name
#         else:
#             print("name的长度必须要大于1个长度")
#     def get_age(self):
#         return self.__age
#     def set_age(self, age):
#         if age > 0 and age < 150:
#             self.__age = age
#         else:
#             print("输入的年龄必须要大于0，小于150岁")
#
# one = Student('plf',18,'男')
# one.set_name('a')       # 通过自己设置接口，可以有效规避脏数据
# print(one.get_name())       # 通过接口获取数据
# one.set_age(-9)         # 通过自己设置接口，可以有效规避脏数据
# print(one.get_age())    # 通过接口获取数据
# 这样我们就自定义了自己属性的接口，它的好处在于：规避脏数据

# 问题：使用接口设置获取数据 和 使用点方法（one.name = 18 或者print(one.name)）设置数据相比， 点方法使用更方便，
# 我们有什么方法达到 既能使用点方法，同时又能让点方法直接调用到我们的接口了？其实python已经帮我们实现了，使用 @property
# 第四阶段：
class Student(object):

    def __init__(self,name,age,sex):
        self.__name = name
        self.__age = age
        self.__sex = sex

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        if len(name) > 1 :
            self.__name = name
        else:
            print("name的长度必须要大于1个长度")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age > 0 and age < 150:
            self.__age = age
        else:
            print("输入的年龄必须要大于0，小于150岁")


one = Student('plf',18,'男')

one.name = '张三'
print(one.name)

one.age = 170
print(one.age)

#总结：
# 使用 @property 装饰器时，接口名不必与属性名相同.
# 凡是赋值语句，就会触发set方法。获取属性值，会触发get方法

