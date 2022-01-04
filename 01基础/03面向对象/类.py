# 类：具有相同属性和技能的一类事物
# 对象： 类的具体表现

# class Person: # 类名首字母大写
#     name = "沈万三"
#     age = "25"
#     dynasty = "明朝"
#
#     def __init__(self, sex):
#         # print(self) # 类实例化成对象的内存地址
#         self.sex = sex # 相当于给对象添加属性 Person.sex = "男"
#         print("聚宝盆")
#     def say(self):
#         print("贵出如粪土，贱取如珠玉")

# 直接通过类调用方法和属性
# print(Person.__dict__)
# print(Person.name)
# Person.say(1)
# Person.sex = "男" # 给对象添加属性
# print(Person.sex)

# 类实例化成对象，调用属性和方法
# person = Person('男') # 类的实例化， 实例化会自动执行 __init__ 的方法
# print(person) # 改对象的内存地址和 self 一样
# print(person.name)
# person.say()
#print(person.sex)
# person.hight = 175 # 对象添加属性
# print(person.hight)
# person.name = "朱元璋" # 修改属性
# print(person.name)


'''
模拟英雄联盟写一个游戏人物的类
    要求：
    （1）：创建一个Game_role的类
    （2）：构造方法中给对象封装name, ad(攻击力), hp（血量）三个属性
    （3）：创建一个 attack 方法，此方法是实例化两个对象，互相攻击的功能：
        例：实例化一个对象，盖伦， ad 为 10， hp为100
            实例化另一个对象，剑豪， ad为20， hp为80
            盖伦通过attack方法攻击剑豪，此方法要完成“谁攻击谁，谁掉多少血，不剩多少血”的提示功能
'''

class Game_role:
    def __init__(self, name, ad, hp):
        self.name = name
        self.ad = ad
        self.hp = hp

    def attack(self, p):
        p.hp = p.hp - self.ad # 剑豪的血量减去盖伦攻击的血量，就是剑豪剩余的血量
        print('%s攻击%s, %s掉%s血, 还剩%s血' %(self.name, p.name, p.name, self.ad, p.hp) )

gailun = Game_role("盖伦", 10, 100)
jianhao = Game_role("剑豪", 20, 80)
gailun.attack(jianhao)

#print(p2.hp)
