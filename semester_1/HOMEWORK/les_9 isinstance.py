
# 1. Вывести на экран только значения списка, кортежа и множества без кавычек:
for val in [1, 2, 3, 4, 5, [6, 7, 8, 5, 6], (4, 5, 6)]: 
    if isinstance(val, (list, set, tuple)): 
        for i in val: # здесь выводится значения внутри списка [6, 7, 8, 5, 6] и значения внутри кортежа
            print(i)
    elif isinstance (val,(int,str)): # здесь выводятся все значения в списке
            print(val) 

# # 3 -задание
# """
# Используя цикл, написать программу для создания спика чисел из другого списка, умножив все числа внутри списка на 4.
# Пример: Скажем у нас есть список [1, 2, 3, 4, 5, 6, 7] - нужно из него создать другой список, где все числа умножены 
# на 4, то есть ответ должен быть таким -> [4, 8, 12, 16, 20, 24]

# # """
# print("2-задание")
# a=[1,2,3,4,5,6,7]
# b=[]
# print(b)
# for val in a:
#     b.append(val*4)
# print(b)

# ========================================================================================================

# """
# Доп для 3 задания. Изменить программу так, чтобы оно создавало новый список только из численных значений внутри списка, 
# то есть:
# Если есть список -  [1, 2, "hello", 4, 5, 6, 7] - на ответ создать список - [4, 8, 16, 20, 24]"""

a=[1, 2, "hello", 4, 5, 6, 7]
b=[]
for val in a:
    if isinstance (val,(int,float)):
        b.append (val*4)  # [4, 8, 16, 20, 24, 28]
print("3-задание:", b)


# List filtering -- In this kata you will create a function that takes a # list of non-negative integers 
# and strings and returns a new list with the strings filtered out.
# https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/train/python

def filter_list(l):
    result=[]
    for i in l: 
        if isinstance(i,(int, float)):
            result.append(i)
    return result
print(filter_list([1,2,'aasf','1','123',123]))  # Output: [1, 2, 123]

# ======================================================================
# Better solution
def filter_list(l):
    'return a new list with the strings filtered out'
    return [i for i in l if not isinstance(i, str)]

print(filter_list([1,2,'aasf','1','123',123]))  # Output: [1, 2, 123]


