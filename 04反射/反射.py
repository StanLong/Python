# 反射
# 用字符串数据类型的变量来访问这个变量的值

class Student:
    ROLE = 'ROLE'
    def check_course(self):
        print('选课')

    @staticmethod
    def login():
        print('登录')

    @classmethod
    def logout(cls):
        print('登出')

# # 类反射
# print(Student.ROLE)
# # getattr  第一个参数是 . 前面的命名空间(类，或则对象)  第二个参数是 . 后面的字符串形式变量名或者方法名
# # 使用反射查看类中的属性
# print(getattr(Student, 'ROLE'))
#
# # 使用反射调用类中的普通方法
# getattr(Student, 'check_course')(11)
#
# # 使用反射调用类中的静态方法
# getattr(Student, 'login')() # 登录
#
# # 使用反射调用类中的类方法
# getattr(Student, 'logout')() # 登出
#
# # hasattr 判断在第一个参数（命名空间）里有没有以第二个参数作为名称的属性或者方法
# print(hasattr(Student, 'ROLE')) # True
# print(hasattr(Student, 'role')) # False

########################################################################################################################
# 对象反射
student = Student()
# 使用反射查看类中的属性
print(getattr(student, 'ROLE'))

# 使用反射调用类中的普通方法
getattr(student, 'check_course')()

# 使用反射调用类中的静态方法
getattr(student, 'login')() # 登录

# 使用反射调用类中的类方法
getattr(student, 'logout')() # 登出

########################################################################################################################

# setattr(object, name, value)
# 给object对象的name属性赋值value，如果对象原本存在给定的属性name，则setattr会更改属性的值为给定的value；
# 如果对象原本不存在属性name，setattr会在对象中创建属性，并赋值为给定的value
setattr(student, 'NAME', '沈万三')
print(getattr(student, 'NAME'))

# 删除属性
delattr(student, 'NAME')
print(getattr(student, 'NAME')) # AttributeError: 'Student' object has no attribute 'NAME'
