# 组合： 一个类的对象作为另一个类的对象的属性，称为类的组合

# 先定义三个类：人、汽车、手机
class Person:
    def __init__(self,name,sex,age,position):
        self.name = name
        self.sex = sex
        self.age = age
        self.position = position

class Car:
    def __init__(self,brand,price,color):
        self.brand = brand
        self.price = price
        self.color = color

class Phone:
    def __init__(self,brand):
        self.brand = brand

    def call_up(self):
        print("I'm calling you...")

#  对于这三个类来说，各自独立又有联系，人可以拥有手机，人也可以拥有一辆汽车
jack = Person('jack','male',35,'Manager')   #实例化一个人
jack.car= Car(brand = 'Cadillac',price = 200000,color = 'Red')  #给人新增一个车的属性，即人可以拥有一辆车，并实例化一辆车，再赋值给属性
jack.phone = Phone('SamSung')   #原理同上

# 属性与方法的调用
print(jack.car.brand)   #注意属性之间的调用写法顺序
print(jack.car.color)
print(jack.car.price)
print(jack.phone.brand)
jack.phone.call_up()