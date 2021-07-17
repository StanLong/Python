# 冒泡排序
# a = [4,3,5,1,6,7,8,0,2,9]
# for i in range(a.__len__()-1, -1, -1):
#     for j in range(0, i, 1):
#         if a[i] < a[j]:
#             temp = a[i]
#             a[i] = a[j]
#             a[j] = temp
# for i in a:
#     print(i)

# 选择排序
# a = [4,3,5,1,6,7,8,0,2,9]
# for i in range(0, a.__len__() , 1):
#     # 假设下标 min 为数组元素最小的下标
#     min = i
#     for j in range(i+1, a.__len__(), 1):
#         if a[j] < a[min]:
#             min = j
#
#     if i != min:
#         temp = a[min]
#         a[min] = a[i]
#         a[i] = temp
#
# for i in a:
#     print(i)

# 二分法查找

def binary_search(a, dest_element):
    begin = 0
    end = a.__len__()-1
    while begin <= end:
        mid = (begin + end) // 2 # // 表示整除
        if a[mid] == dest_element:
            return mid
        elif a[mid] > dest_element:
            end = mid -1
        elif a[mid] < dest_element:
            begin = mid +1
    else:
        return -1


if __name__ == '__main__':
    a = [1,2,3,4,5,6,7,8,9,10]
    dest_element = 11
    index = binary_search(a, dest_element)
    print("%d 在列表中不存在" %dest_element if index == -1 else "%d 在列表中的下标是 %d" %(dest_element, index))

