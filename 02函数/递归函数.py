# 使用递归遍历目录树
# import os
# file_path = 'D:\StanLong\git_repository\Python'
# def func(file_path, n): # n 是递归深度
#     file_list = os.listdir(file_path)
#     for file in file_list:
#         if os.path.isdir(os.path.join(file_path, file)): # 判断file是否是个目录
#             print("\t" * n, file)  # 打印文件夹
#             # 如果时目录，继续调用 func。 这里是递归的入口
#             func(os.path.join(file_path, file), n+1)
#         else:
#             print("\t"*n, file) # 递归的出口， 打印文件
# func(file_path, 0)

# 递归计算斐波那契数列第n项的数据
# def func(n):
#     # 给递归一个出口  第一位和第二位都是1
#     if n == 1 or n == 2:
#         return 1
#     else:
#         # 从第三位开始  返回上一个数加上上一个数
#         return func(n-1) + func(n-2)
# res = func(20)
# print(res)

# 递归计算斐波那契数列第n项的数据
# fib = lambda n : n if n <= 2 else fib(n-1)+fib(n-2)
# print(fib(2))


# 二分查找
# 必须是有序列表才能使用二分查找

# 纯算法
# target = 3 # 要查找的数据
# lst = [0,1,2,3,4,5,6,7,8,9]
# left = 0
# right = len(lst) - 1
#
# while left < right:
#     middle = (left + right) // 2  # // 是整除
#     if lst[middle] < target:
#         left = lst[middle]
#     elif lst[middle] > target:
#         right = lst[middle]
#     else:
#         print("目标值%s" %target, "找到了%s"%lst[middle])
#         break
# else:
#     print("不存在")