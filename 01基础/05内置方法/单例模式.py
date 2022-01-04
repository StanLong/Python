# 单例模式
# 一个类只能有一个实例

class Single:
    __ISINSTANCE = None
    def __new__(cls, *args, **kwargs):
        if not cls.__ISINSTANCE:
            cls.__ISINSTANCE = super().__new__(cls)
        return cls.__ISINSTANCE
    def __init__(self):
        pass
s1 = Single()
print(s1) # <__main__.Single object at 0x000001910CA7B748>
s2 = Single()
print(s2) # <__main__.Single object at 0x000001910CA7B748>