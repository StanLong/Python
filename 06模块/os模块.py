import os
print(os.getcwd()) # 当前文件的工作路径
# D:\StanLong\git_repository\Python\06模块
# os.chdir('D:\StanLong\git_repository\Python\06模块') # 手动改变文件的工作路径
# os.mkdir('dira') # 在当前路径创建单极目录
# os.makedirs('dirb/dirc/dird') # 在当前路径创建多级目录
# os.rmdir('dira') # 删除单极目录， 不能删除非空文件夹
# os.removedirs('dirb/dirc/dird') # 删除多极目录

# print(os.listdir('../06模块')) # 列出指定目录下的文件和文件夹
# print(os.stat('../06模块')) # 查看文件的元数据信息
# print(os.sep) # 查看当前系统的目录分隔符
# print([os.linesep]) # 打印当前系统的行终止符
# ['\r\n']
# print(os.pathsep) # 输出用于分隔文件路径的字符串 win下是; linux下是:
# print(os.name) # 查看当前平台， win是'nt'， linux是 'posix'

# os.system('dir') # 执行操作系统命令
# par = os.popen('dir') #
# print(par)
# <os._wrap_close object at 0x0000017FC553ADC8>
# print(par.read())
# 当执行增删改动作时，使用 os.system(),
# 当查看执行结果时， 使用 os.popen()

# print(os.environ) # 查看环境变量