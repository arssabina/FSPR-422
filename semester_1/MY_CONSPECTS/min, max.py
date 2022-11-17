# если кортеж состоит из однотипных элементов,  можем их сравнить (числа можно сравнить)
# можем использовать функцию min и max

# a=1,2,3,4,5
# print(min(a), max(a))   # 1 5

# a=1,2,3,4,5, 'hello'
# print(min(a), max(a))    # TypeError: '<' not supported between instances of 'str' and 'int' 
                             # потому что числа со строками нельзя сравнить


# string = "raj" 
# print(min(string))   #   находит мин.значение в алфавитном порядке      # вывод: а

# 1. Создать функцию, которая возвращает длину наименьшей строки  

# my_list=min("ABCDEF", "GHI", "JKLMNO", key=len)
# print(len(my_list), my_list)