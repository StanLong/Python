# 随机生成大乐透中奖组合
# 当然，是否中奖也随机

import random

# 生成两个蓝色球
def blue():
    lst = []
    while True:
        for i in range(2):
            data = random.randrange(1,13)
            lst.append(data)
        if set(lst).__len__() == 2:
            break
        else:
            lst = []
    return sorted(lst)

# 生成指定范围的红色球
def red(start, end):
    lst = []
    while True:
        for i in range(5):
            data = random.randrange(start, end)
            lst.append(data)
        if set(lst).__len__() == 5:
            break
        else:
            lst = []
    return sorted(lst)

if __name__ == '__main__':
    count = 0
    results = []
    loop_count = random.randint(1, 21425712)
    while True:
        if count == loop_count:
            break
        else:

            count = count + 1
            red1 = red(1, 36)
            red2 = red(1, 36)
            red3 = red(1, 36)
            red4 = red(1, 36)
            red5 = red(1, 36)
    results.append(red1)
    results.append(red2)
    results.append(red3)
    results.append(red4)
    results.append(red5)
    print("经过 %s 次的实验，中三等奖的组合是：" %(count))
    for daletou in results:
        print(daletou + blue())