def long_names(x):
    return len(x) >=3

names=['Sa', 'Muhammad', 'Farina', 'Hanifa', 'Asmira', 'Bohir']
print(list(filter(lambda x: len(x) >= 3, names)))
print(list(filter(long_names, names)))

"""
Функция filter предназначена для "фильтрации" массива и может заменить цикл. Filter работает быстрее цикла, в некоторых случаях 
скорость работы программы увеличивается в десятки раз при использовании filter, вместо классических циклов.

Функция filter принимает на вход: - Другую функцию, которая возвращает True или False
                                  - Cписок, элементы которого будут подаваться на вход функции

В функции, передаваемой в filter, должно содержатся условие, которое определяет критерии для элементов нового массива. Если функция возвращает True - элемент добавляется в новый массив, если False - элемент не добавляется.

Функция filter возвращает объект класса Filter, используйте list(), чтобы переделать его в массив
"""

numbers = [20, 30, 40, 50, 60]

# 1-метод
result = []
for num in numbers: 
    if num > 40:
        result.append(num)
print(result)

# 2-метод    # with filter func: 
def nums(num):
    return num > 40

print(list(filter(nums, numbers)))

# 3-метод with lambda
print(list(filter(lambda x : x > 40, numbers)))

# ====================================================

def f(x): 
    return x > 10 and x < 40

num_list = [1, 15, 64, 98, 32, 21, 18, 36]

print(list(filter(f, num_list)))  
result = [i for i in num_list if i > 10 and i < 40] # с генератором списка
print(list(filter(lambda x : x > 10 and x < 40, num_list))) # с помощью lambda
print(result)

new_list = [1, 'sssd', 15, 64, '', 98, 32, '  ', 21, [25, 63], 18, 36]
print("True elements: ", list(filter(bool, new_list)))
print("True elements: ", list(filter(None, new_list)))


s = 'Sabina1212'
print("Only digits: ", list(filter(str.isdigit, s)))
print("Only letters: ", list(filter(str.isalpha, s)))
print("Upper letters: ", list(filter(str.isupper, s)))



s_list = ['name', 'frame', 'time', '', 'shame', ' ', 'func']
# print("Ends with 'ame': ", list(filter(str.endswith('ame'), s_list ))) ошибка???????
res = list(filter(lambda x : x.endswith('ame'), s_list))
print(res)

python_dict={
    "set"  : "множество",
    "dict" : "словарь",
    "tuple" : "кортеж",
    "list" : "список",
    "str" : "строка",
}
s = list(filter(lambda x : len(x) > 3, python_dict))
print(s)

my_dict = {
    'Ann' : 12, 
    'George': 26, 
    'Peter' : 32,
    'Tom' : 38,
}
s_1 = list(filter(lambda x : my_dict[x] > 26, my_dict))
print("Выводит ключи, значения кот.больше 26: ", s_1)

