# 有1000名，如果员工的姓名，性别相同，则认为是同一个员工

#解
# 封装类
class Employee:
    def __init__(self, name, age, sex, partment):
        self.name = name
        self.age = age
        self.sex = sex
        self.partment = partment
    # 如果员工的姓名，性别相同，则认为是同一个员工
    def __eq__(self, other):
        if self.name == other.name and self.sex == other.sex:
            return True
    def __hash__(self):
        return hash('%s%s'%(self.name, self.sex))

# 数据准备
employee_list = []
for i in range(100):
    employee_list.append(Employee('沈万三', i, '男', '商务部'))
for i in range(100):
    employee_list.append(Employee("徐达", i, '男', '国防部'))
for i in range(100):
    employee_list.append(Employee("朱元璋", i, '男', '皇帝'))

# 去重
# set的去重是通过两个函数__hash__和__eq__结合实现的。
# 1、当两个变量的哈希值不相同时，就认为这两个变量是不同的
# 2、当两个变量哈希值一样时，调用__eq__方法，当返回值为True时认为这两个变量是同一个，应该去除一个。返回FALSE时，不去重
employee_set = set(employee_list) # set的去重是通过两个函数__hash__和__eq__结合实现的
for person in employee_set:
    print(person.__dict__) # 在没有实现hash方法时，这一步报错 unhashable type: 'Employee'

