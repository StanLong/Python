# random 模块
# import random
# print(random.random()) # 0-1之内的随机小数
# print(random.uniform(1,10)) # 1到10之内的随机小数
#
# print(random.randint(1,10)) # 1到10内随机整数
# print(random.randrange(1,10)) # 1到10之内的随机整数， 不包含10
# print(random.randrange(1,10,2)) # 1到10之内的随机奇数， 不包含10
#
# lst = ['1','2','3','a','b','c']
# print(random.choice(lst)) # 从列表中随机抽取一个值
# print(random.sample(lst, 2)) # 从列表中随机抽取多个
# random.shuffle(lst) # 打乱原列表的顺序
# print(lst)


# 生成一个四位的随机验证码
# import random
# code = ''
# for i in range(4):
#     code = code + str(random.randint(0, 9))
# print(code)

# 生成一个任意长度的数字验证码
# import random
# def rand_code(n):
#     code = ''
#     for i in range(n):
#         num = random.randint(0,9)
#         code = code + str(num)
#     return code
#
# if __name__ == '__main__':
#     code = rand_code(6)
#     print(code)

# 生成一个六位数字+字母的验证码
# import random
# c = ''
# for i in range(6):
#     a = str(chr(random.randint(97, 122)))
#     b = str(random.randint(0, 9))
#     c = c + random.choice([a,b])
# print(c)

# 高级版
# 可生成任意个数的数字和字符随机组合密码
import random
def rand_code(n=6, alph_flag = True):
    code = ''
    for i in range(n):
        rand_num = str(random.randint(0,9))
        if alph_flag:
            rand_alph = str(chr(random.randint(97,122)))
        code = code + random.choice([rand_num, rand_alph])
    return code

if __name__ == '__main__':
    code = rand_code(4)
    print(code)