# sorted 排序函数
# 语法
# sorted(Iterable, key=None, reverse=False)
# Iterable 可迭代对象
# key 排序规则
# resverse

# lst = [1,4,3,2,5]
# lst.sort()
# print(lst)
# [1, 2, 3, 4, 5]

# ll = sorted(lst)
# print(ll)
# [1, 2, 3, 4, 5]

# ll = sorted(lst, reverse=True)
# print(ll)
# [5, 4, 3, 2, 1]

# 列表排序，要求根据字符串的长度排序
# lst_name = ['沈万三', '苏半城', '雪娥', '南海财神']
# ln = sorted(lst_name, key=lambda s : len(s)) # 可以把迭代对象中的每一个元素传给 lambda
# print(ln)
# ['雪娥', '沈万三', '苏半城', '南海财神']

# 字典排序
lst = [{'id':3, 'name':'刘伯温', 'age':55},
       {'id':1, 'name':'沈万三', 'age':24},
       {'id':2, 'name':'朱元璋', 'age':30}
    ]
ll = sorted(lst, key=lambda dic:dic['age'])
print(ll)
# [{'id': 1, 'name': '沈万三', 'age': 24}, {'id': 2, 'name': '朱元璋', 'age': 30}, {'id': 3, 'name': '刘伯温', 'age': 55}]

