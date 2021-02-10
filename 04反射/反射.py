# 反射
# 用字符串数据类型的变量来访问这个变量的值

# 类反射
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

student = Student()
print(student.ROLE)
# getattr  第一个参数是 . 前面的对象(命名空间)  第二个参数是 . 后面的字符串形式变量名或者方法名
# 使用反射查看类中的属性
print(getattr(student, 'ROLE'))

# 使用反射调用类中的普通方法
print(getattr(student, 'check_course')) # <bound method Student.check_course of <__main__.Student object at 0x000002475A4AB608>>
getattr(student, 'check_course')() # 选课

# 使用反射调用类中的静态方法
getattr(student, 'login')() # 登录

# 使用反射调用类中的类方法
getattr(student, 'logout')() # 登出

# hasattr 判断在第一个参数（对象或者命名空间）里有没有以第二个参数作为名称的属性或者方法
print(hasattr(student, 'ROLE')) # True
print(hasattr(student, 'role')) # False