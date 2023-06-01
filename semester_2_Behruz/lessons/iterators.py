# USERS=[
#     {   'name': 'Sabina',
#         'email': 'sa@',
#         'password': '123456',
#         'purchases': [],
#         'card': {'code': '1234567891234567', 'balance': 1000}
#     }
# ]

# def register(name, email, password, card_code, card_balance):
#         # Есть ли данный пользователь в системе
#         for user in USERS:
#             if user['email'] == email and user['password'] == password:
#                 return "Пользователь с такими данными уже есть."

#         if not (name and email and password and card_code and card_balance):
#             return 'Empty values were given.'
#         try:
#             name.isalpha() and '@' in email and len(password) >= 6 and len(card_code) == 16 and card_balance >= 0
#             USERS.append(
#                 {
#                     'name': name,
#                     'password': password,
#                     'email': email,
#                     'purchases': [],
#                     'card': {'code': card_code, 'balance': card_balance}
#                 }
#             )
#         except TypeError as err:
#             print("Error happened", err)
#         except  AttributeError as err:
#             print("Error happened", err)
#         except  ValueError as err:
#             print("Error happened", err)
             
    
# register('kdfgbsrjh', 'tamina@', 10003, '1234567891234566', 2000) 

# class UserAgeIsLessThanEighteen(Exception):
#     """The user should be above 18"""
# user = {
#     'age': 12, 
#     'name': 'nbh',
        
# }

# if user['age'] < 18:
#     raise UserAgeIsLessThanEighteen()


# class InvalidAgeException(Exception):
#     """Raise when the input value is less than 18"""
#     pass

# number = 18

# try:
#     input_num = int(input("Enter the number: "))
#     if input_num < 18:
#         raise InvalidAgeException()
#     else: 
#         print("Eligible to vote")

# except InvalidAgeException: 
#     print("Exception occured: Invalid age")

# ===========================================================
# Дополняем логику сообщения об ошибке:
def SalarynotInRangeError(Exception): 
    """Exception raised for errors in the input salary
    Arguments:
    salary = input salary which caused the error, 
    message = explanation of the error"""


# class LenNameLessThenfive(Exception):
#     """The user's name len should be more then five letters"""
# user = {
#     'age': 12, 
#     'name': 'nbh',
        
# }

# try: 
#     len(user['name']) < 3:
# except:
# if len(user['name']) < 3:
#     raise LenNameLessThenfive()


# =====================================================================
# Iterators:
"""
Итерируемые переменные - это те переменные, кот.содержат  более одного значения. 
(str, dict, set, list, tuple)

Только из итерируемқх переменных можно создать итераторы(итератор объекты). 

Можно итер объект создать двумя способами: 
1) s = [2,4,6,8,10]
s_iter = iter(s)
2) c помощью магической функции:
s = [2,4,6,8,10]
s_iter = s.__iter__()

Итерируемый объект при передаче в функцию iter() возвращает итератор.
Итератор,при передаче в функцию next() возвращает следующий элемент или вызывает StopIteration после того, как все элементы будут
исчерпаны. при передаче функции iter() возвращает себя.
Протокол итератора – это не что иное, как стандартный способ определения объектов как итераторов. Мы уже видели протокол в действии в предыдущем разделе. Согласно протоколу, итераторы должны определить следующие два метода:

__next()__
Этот метод должен возвращать следующий элемент серии каждый раз, когда он вызывается. Как только все элементы исчерпаны, должно
появиться исключение StopIteration.
Этот метод вызывается изнутри, когда мы вызываем встроенный метод next().
__iter()__
Этот метод должен возвращать сам объект итератора.
Это метод, который вызывается внутри, когда мы вызываем встроенный метод iter()."""

dog_foods = {
    "Great Dane Foods": 4, 
    "Min Pin Pup Foods": 10,
    "Pawsome Pups Foods": 8

}
for food_brand in dog_foods: 
    print(food_brand + 'has' + str(dog_foods[food_brand]) + " bags")

dog_foods_iterator = iter(dog_foods) # создание итератора из итер.переменной

print(dog_foods_iterator)
a = next(dog_foods_iterator)
print(a)
"""Если создавать копию из самого итератора, то два итератора работают вместе, продолжают работу друг-друга, но если создать 
итератор от самой итер переменной, тогда создаётся новый итератор """
"""В чем разница между итератором и циклом?
В отсутствие вызовов итератора оператор цикла просто выполняет бесконечный цикл. Разница между вызовом итератора и
вызовом подпрограммы заключается в том, что вызов итератора «запоминает» свое состояние после получения значения и при последующих вызовах просто возобновляет выполнение ."""
dog_foods_iterator_two = iter(dog_foods)
print(dog_foods_iterator_two)
b = next(dog_foods_iterator_two)
print(b)

b = next(dog_foods_iterator_two)
print(b)

b = next(dog_foods_iterator_two)
print(b)

# c = (map(next, dog_foods_iterator))
# print(c)

# c = (map(next, dog_foods_iterator))
# print(c)

dog_foods_iter = iter(dog_foods)

while True:
    try: 
        print(next(dog_foods_iter))
    except StopIteration:
        break
    
