# __item__ 系列
# obj[变量名]  实际上调用了内部的__getitem__(self,item)方法
class B:
    def __getitem__(self, item):
        print(item)
        return '__getitem__'
    def __setitem__(self, key, value):
        print(key, value)
    def __delitem__(self, key):
        print(key)
b = B()
print(b['a']) # 触发了 __getitem__ 方法
b['name'] = '沈万三' # 触发了 __setitem__ 方法
del b['name']       # 触发了 __delitem__ 方法

# hash 方法
# 底层数据结构基于hash寻址的优化操作
# 对同一个值在多次执行python代码的时候hash值不同
# 但是对同一个值 在同一次执行python代码的时候，hash值永远不变
print(hash('abc'))
print(hash('abc'))
print(hash('abc'))


# eq 方法
class A:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __eq__(self, other):
        if self.name == other.name and self.age == other.age:
            return True
a = A('沈万三', 30)
aa = A('沈万三', 30)
print(a == aa) # == 触发 __eq__ 方法