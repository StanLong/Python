# 类：具有相同属性和技能的一类事物
# 对象： 类的具体表现

class Person: # 类名首字母大写
    name = "沈万三"
    age = "25"
    dynasty = "明朝"

    def __init__(self, sex):
        # print(self) # 类实例化成对象的内存地址
        self.sex = sex # 相当于给对象添加属性 Person.sex = "男"
        print("聚宝盆")
    def say(self):
        print("贵出如粪土，贱取如珠玉")

# 直接通过类调用方法和属性
# print(Person.__dict__)
# print(Person.name)
# Person.say(1)
# Person.sex = "男" # 给对象添加属性
# print(Person.sex)

# 类实例化成对象，调用属性和方法
person = Person('男') # 类的实例化， 实例化会自动执行 __init__ 的方法
# print(person) # 改对象的内存地址和 self 一样
# print(person.name)
# person.say()
#print(person.sex)
person.hight = 175 # 对象添加属性
print(person.hight)
person.name = "朱元璋" # 修改属性
print(person.name)