import sys

print(sys.argv)
# C:\Users\Administrator>python D:\StanLong\git_repository\Python\06模块\sys模块.py abc
# ['D:\\StanLong\\git_repository\\Python\\06模块\\sys模块.py', 'abc']

# C:\Users\Administrator>python D:\StanLong\git_repository\Python\06模块\sys模块.py abc abcd
# ['D:\\StanLong\\git_repository\\Python\\06模块\\sys模块.py', 'abc', 'abcd']
# 文件名后面可直接跟参数， 多个参数都会被依次添加到列表中