# 继承：子类获得了父类的全部属性及功能

class Person(object):
    def __init__(self,name,sex):
        self.name = name
        self.sex = sex

    def print_title(self):
        if self.sex == "male":
            print("man")
        elif self.sex == "female":
            print("woman")

class Child(Person):         # Child 继承 Person
    # def __init__(self, name, sex, age): # 子类自定义初始化方法
    #     self.name = name
    #     self.sex = sex
    #     self.age = age

    def __init__(self, name, sex, age):
        #Person.__init__(self,name,sex) # 使用父类的初始化方法 可用super关键字代替
        super().__init__(name, sex)
        self.age = age
    def print_title(self):   # 当子类和父类都存在相同的 print_title()方法时，子类的 print_title() 覆盖了父类的 print_title()，在代码运行时，会调用子类的 print_title()这样，这就是继承的另一个好处：多态
        print("子类")


May = Child("May","female",18)
Peter = Person("Peter","male")

print(May.name,May.sex, May.age, Peter.name,Peter.sex)    # 子类继承父类方法及属性
May.print_title()
Peter.print_title()