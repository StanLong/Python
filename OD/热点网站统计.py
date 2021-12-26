def cal(num1, num2, oper):
    if oper == '+':
        return num1 + num2
    if oper == '-':
        return num2 - num1
    if oper == '*':
        return num1 * num2
    if oper == '/':
        return num2 / num1

print(cal(1,2, '+'))
print(cal(1,2, '-'))
print(cal(1,2, '*'))
print(cal(1,2, '/'))
