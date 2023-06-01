# class FishInventory:
#     def __init__(self, fishList):
#         self.available_fish = fishList

#     def __iter__(self):
#         self.index = 0
#         return self
        
    
#     def __next__(self):
#         if self.index < len(self.available_fish):
#             fish_status = self.available_fish[self.index]
#             self.index += 1
#             return fish_status
#         else: 
#             raise StopIteration


# fish_inventory_cls = FishInventory(['Bubbles', 'Finley', 'Moby'])
# for fish in fish_inventory_cls:
#     print(fish)

# ==============================
# создайте для класс CustomerCounter методы iter и next, которые 
# возвращать число пользователей и остановиться, когда их число 
# превышает 100


# class CustomerCounter:
#     def __init__(self, customerList):
#         self.customers = customerList

#     def __iter__(self):
#         self.count = 0
#         return self
        
#     def __next__(self):
#         if self.count > 99:
#             raise StopIteration
#         self.count += 1
#         return self.count

       
# customer_cls = CustomerCounter(list(range(110)))
# for customer in customer_cls:
#     print(customer)
# ========================================================================

from itertools import count, chain, combinations 

#count(start, [step])
for i in count(start = 0, step =2):
    # он принимает начало и шаг
    print(i)
    if i >= 20:
        break

odd = [5,7,9]
even = {10,12,14}
# ==========================================
all_numbers = chain(odd, even)
# соединяет две переменные в список, сперва идёт первый список, потом второй
for num in all_numbers:
    print(num)

# ===============================================
even = [2,4,6]
even_combinations = list(combinations(even, 2))
    # он принимает два аргумента: переменную и кол-во комбинаций 

print(even_combinations)
# [(2, 4), (2, 6), (4, 6)]
# combination = возвращает кол-во возможных комбинаций списка

# collars = ['red-s', 'red-x', 'blue-xs', 'green-l', 'yellow-m']
# collars_combo_iterator = combinations(collars, 3)

# for collar in collars_combo_iterator:
#     print(collar)

# ===========================================================

# ФУНКЦИЯ ГЕНЕРАТОР

"""Yield — это ключевое слово в Python, которое используется для возврата из функции с сохранением состояния ее локальных переменных,
и при повторном вызове такой функции выполнение продолжается с оператора yield, на котором ее работа была прервана. 
Любая функция, содержащая ключевое слово yield, называется генератором."""
def get_list():
    for x in[1,2,3,4]:
        yield x

a=get_list()

# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a)) # stopIteration

# for x in a:
#     print(x)

# # ======================================================

# def fib(n):
#     if n==1:
#         return 0
#     if n==2:
#         return 1
#     else: 
#         return fib(n-1)+fib(n-2)

# print(fib(5))

# Generator expressions
print((i for i in range(100000000)))
def multiply(a,b):
    sum=0
    return a*b

print(multiply(3,6))

def course_generator():
    yield 'Computer Science'
    yield 'Art'
    yield 'Business'

courses=course_generator()
for course in courses:
    print(course)

# ---------------------------------------------------------


# ---------------------------------------------------------
def prize_generator():
    student_info={
        'Joan Tsark':355,
        'Bekzod':123,
        'Sabina':12,
        'Kate':45

    }

    for student in student_info:
        name=student
        id=student_info[name]
        if id%3==0 and id%5==0:
            yield student+"Get prize C"
        elif id%3==0:
            yield student+"Get prize B"
        elif id%5==0:
            yield student+"Get prize A"

prizes=prize_generator()
for prize in prizes:
    print(prize)


def factorial_generator(n):
    term = 1

    for i in range: 
        c = term * i
        yield c
        term = c

fact = factorial_generator

