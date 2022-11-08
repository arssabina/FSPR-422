# Важнейшей функцией, которую вы будете использовать для сортировки словарей, является встроенная sorted()функция. 
# Эта функция принимает итерируемый объект в качестве основного аргумента с двумя необязательными аргументами, 
# состоящими только из ключевых слов, — keyфункцией и reverseлогическим значением.

# sorted()функция принимает итерируемый объект, сортирует сопоставимые элементы, такие как числа, 
# в порядке возрастания и возвращает новый список. Строки сортируются в алфавитном порядке:

# sorted()заключается в том, что он возвращает список, а не словарь

# words = ["ab", "aa", "ac", "bc", "cb", "ca"]
# print(sorted(words))  # ['aa', 'ab', 'ac', 'bc', 'ca', 'cb']

# numbers = [5, 3, 4, 3, 6, 7, 3, 2, 3, 4, 1]
# print(sorted(numbers))    #   [1, 2, 3, 3, 3, 3, 4, 4, 5, 6, 7]

# dict = {3:"hello", 2:"hello", 1:"hello"} 
# d_1 = sorted(dict.keys()) 
# print(d_1)      #  [1, 2, 3] sorts the keys of dict and gives a list with only keys

# dict = {3:"hello", 2:"hello", 1:"hello"}
# d_1 = sorted(dict.items())
# print(d_1)       # sorts the the keys of dict and gives a list with keys and values of the dict

# cars=['bmw', 'audi', 'toyota', 'subaru']
# print(sorted(cars))        # # => ['audi', 'bmw', 'subaru', 'toyota']
# print(cars)

# sorted - временно сортирует список.
# sort - изменяем и сортирует список. список изменяется на постоянной основе

# cars=['bmw', 'audi', 'toyota', 'subaru']
# cars.sort()
# print(cars)     # ['audi', 'bmw', 'subaru', 'toyota']


# # Сортировка списка в обратном алфавитном порядке
# cars.sort(reverse=True)  # ['toyota', 'subaru', 'bmw', 'audi']
# print(cars)