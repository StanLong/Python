# 切片
expression = "3+2*6-2"
ch = expression[0:1]
print(ch)

# 列表模拟栈的功能
lst = [1,2,3]
lst.push(4) # 入栈
lst.pop() # 弹栈
lst[-1] # 返回栈顶元素

# 定义二维数组
# 方式一:
chessArr1 = []
for i in range(11):
    chessArr1.append([])
    for j in range(11):
        chessArr1[i].append(0)
        
# 方式二:
lst = [([0] * 3) for i in range(4)]