# Вопросы: 
# По 5 баллов 
# 1. Что такое PVM (python virtual machine)? 
# PVM - это часть интерпретатора. Перебирает байт-код  и выполняет все последующие операции.
# 2. Напиши список базовых переменных в питоне, их описание и отличие друг от друга 
# базовые переменные: bin, frozenset, tuple, int, float, str, bool, set, dict, list

# # 3. Какие переменные являются immutable (не изменяемые), а mutable (изменяемые) и разница между ними? 
# не изменяемые: 
# bin, frozenset, tuple, int, float, str, bool
# изменяемые: set, dict, list

# 4. Сколько типов форматирования у строк? Приведи пример на каждый из них 

# 5. В чем различие is от in 
# is сравнивает ID ДВУХ ЗНАЧЕНИЙ
# == Оператор == сравнивает значение двух объектов.
# in проверяют, есть ли значение или переменная в строке, списке, кортеже, множестве или словаре

# # 6. Какие области видимости есть в питоне? 
# local enclosed global built-in
# в питоне есть 4 области видимости: локальная, enclosed, глобальная и встроенная

# 7. Возвращает ли функция что-то, если в ней нету return? Если да, то что? 
# return возвращает значение, если нет return он возвращает None

# ===================================================================================================
# По 10 баллов 
# 1. Создать функцию, которая возвращает длину наименьшей строки  

# my_list=min("ABCDEF", "GHI", "JKLMNO", key=len)
# print(len(my_list), my_list)

# ====================================================================================================
# не поняла!!!!
def short_word(names):
    if names:
        length=len(names[0]) # этот код для проверки того, не пустой ли список  
        # будет 6, потому что длина первой строки из 6 букв
    else:
        return False
    for name in names[1:]:
        name_len=len(name)
        if name_len<length:
            length=name_len
    return length

# names=['Farina', 'Tamina', 'Hanifa']
short_word(['Farina', 'Tamina', 'Hanifa'])

# ================================================================================================

# 2. Написать функцию, которая принимает число (функция должна работать для чисел от 0 до 99) и возвращает её как строку на английском 
# Пример: 
# name_that_number(4)   # returns "four" 
# name_that_number(19)  # returns "nineteen" 
# name_that_number(99)  # returns "ninety nine" 

# n=int(input("Enter number:"))
# first_digit=n//10
# last_digit=n%10
# # print(first_digit, last_digit)
# from_one_to_twenty=['zero','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 
#     'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
# decades=['none', 'ten','twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
# if n<1 or n>=100:
#     print("invalide input")
# if n<20:
#     result=from_one_to_twenty[n]
#     print(result)
# if n>20:
#     result=decades[first_digit] +" " + from_one_to_twenty[last_digit]
#     print(result)
# ==========================================================================================================================

# 3. Создай из строки "You've got that fire (fire). The flavor, the style (style)" - список, первое значени которого хранит -
#  первую фразу, второе - вторую фразу. Результат: ["5/ You've got that fire (fire)", "The flavor, the style (style)"] 
# Правильный вариант:
# my_list=["You've got that fire (fire).", "The flavor, the style (style)"]
# print(my_list[0])
# print(my_list[1])

# Не правильный вариант:
# s_1="You've got that fire (fire). The flavor, the style (style)"
# list="You've got that fire (fire). The flavor, the style (style)"
# result=list [:27]
# result_1=list[28:58]
# message=" '" + result + "' " + ", " + result_1 + "' "
# print(message)

# =========================================================================================================================
# 4. Исправь код ниже. В результате он должен создать список из 9 чисел (удалять что-то из кода нельзя) 
# names = [] 
# for i in range(10): 
#     names.append(i + 4) 
#     if i == 7: 
#         names.pop(0) 
# print(names)
    
# 5. Создать программу, которая проверяет, находиться ли строка "John" в списке names (значения списка можно самому создать), Если 
# строка "John" находится в списке, вывести строку, если нет, вывести -1 

# Правильный вариант: исправленный!!!! 
# names=["Ann", "Peter", "John"]
# if 'John' in names: 
#     print("John")
# else: 
#     print(-1)

# 
# names=["Ann", "Peter", "John"]
# for val in names: 
#     if val=="Ann":
#         continue
#     if val=="Peter":
#         continue
#     if val=="John":
#         print("John")
#     else: 
#         print(-1)

# 6. Создать программу, которая проверяет, есть ли в словаре ключ "race" и "age", где значение ключа "age" должно быть числом. Если 
# проверка прошла, вывести на экран значение "race" и "age", если нет, вывести на экран строку human.
#
# 
#  1-method:====================================

# d={'race': 'first', 'age': 18, 'skill': ['Roar']}
# print(d)
# if 'race' in d and 'age' in d and isinstance (d['age'], int):
#     print(d['race'], d['age'])
# else: 
#     print('Human')

# 2-method======================================

# d={'race': 'first', 'age': 18}
# print(d)
# if d.get('race' or 'age'):
#     values=d.values()
#     print(values)
# else: 
#     print('Human')
