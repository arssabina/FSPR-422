# Функцией map, так же как и функцией filter, можно заменить циклы. Циклы работают медленнее чем map, но не каждый цикл
# можно заменить на map.

# Функция map, принимает на вход: - Функцию, которой передают каждый элемент массива
#                                 - Массив

# Функция map позволяет сделать код красивее и ускорить его работу

# def addition(n):
#     return n + n


# # We double all numbers using map()
# numbers = (1, 2, 3, 4)
# result = map(addition, numbers)
# print(list(result))


numbers=[2,3,4,5,6,7]

# 2-способа:
# ================================= 

def square(x): 
   return x**2

answer=list(map(square, [2,3,4,5,6]))  
# answer=list(map(square, numbers))  
print(answer)
# =====================================

answer_2=list(map(lambda x : x ** 2, numbers))
print("Answers with lambda in map: ", answer_2)


# ============================================

msg=['hello', 'how', 'are you?']

print("Длина строки msg: ", list(map(len, msg)))  # Output: Длина строки msg:  [5, 3, 8]

print("Upper msg: ", list(map(str.upper, msg))) # Output: Upper msg:  ['HELLO', 'HOW', 'ARE YOU?']


print("Вывод всей строки в обратном порядке: ", list(map(lambda x : x[::-1], msg)))
# то же самое с генератором списка:
c = [i[::-1] for i in msg]
print("Вывод всей строки в обратном порядке с генератором списка: ", c)


# Добавление элемента в iterable: 
b = list(map(lambda x : x + '!', msg))
print("Добавили '!' : ", b)


# Разбить каждую строку в список: 
d = list(map(list, msg))
print("Разбить строки в список:", d)

# Теперь будем сортировать вложенные списки, которые мы получили разбив msg на списки в предыдущей команде: 
e = list(map(sorted, d))
print("Сортировка списков: ", e)


# В этом коде числа введённые пользователем через пробел в одной строке, сперва разбиваются на строке с помощью команды 
# split, a затем сохраняем в виде списка)
# f = list(map(int, input().split()))
# print("Числа введённые в одной строке через пробел сохраняем в виде списка:", f)

# в этом коде преобразуем строки в числа: 
# 1-метод
print(list(map(int, ['1', '2', '3'])))

# 2-метод
fav_nums=['12', '15', '5', '18']
num=[int(i) for i in fav_nums ]
print(num)

# Функция map фактически возвращает генератор, генератор это итератор, в котором какая-то функция применяется последовательно 
# к элементам итерируемой последовательности. Функция map исп-ся исключительно для удобства, чтобы  не прописывать генератор,
# в классическом виде:


# Матем.вычитания:
int_str = (list(map(int, fav_nums)))

sum_nums = sum(int_str)
print("Sum nums: ", sum_nums)

max_num = max(int_str)
print("Max.num is: ", max_num)

for x in num: 
   print(x, end = ' - ')

# Узнать длину элементов списка:
cities = ['Tashkent', 'Ankara', 'Stambul']
print("\n""Длина элементов списка: ", list(map(len, cities)))
print("\n""Измняем города на список с заглавными буквами : ", list(map(str.upper, cities)))

# Функция len, upper и остальные встроенные функции передаются как ссылка на функцию, поэтому мы пишем их без круглых скобок

def cities_upper_case(s):
   return list(s.lower())  # В этой команде, наш список преобр.в список из вложенных списков, и в этом вложенном списке 
                           # отдельные символы соответств.строк
print(list(map(cities_upper_case,cities)))

# == или же та же самая команда с lamdda
print(list(map(lambda s : list(s.lower()), cities)))