# Две функции, кот.выполняют одну и ту же работу

def func(x): 
    return x**2

power_of_2 = lambda x: x ** 2
print (power_of_2(2))

numbers=[i for i in range(10)]
print(list(map(power_of_2, numbers)))  # здесь функция maр, как аргумент берёт(1-функию lambda, 2-* итерируемый список - numbers)

# ===========================================

def mult(x, y): 
    print("args", x, y)
    return x * y

power_of_2 = lambda x, y: x * y


# def mult(x,y,z): 
#     print("args", x, y, z)
#     return x * y * z

numbers=[i for i in range(10)]
numbers_2=[i for i in range(10,15)]
numbers_3=[i for i in range(20,30)]

# print(list(map(mult, numbers, numbers_2, numbers_3)))

def add_tax(total):
    tax = total * 0.06
    new_total = total + tax
    return new_total

# функции как аргументы
def total_bill(func, value):
    total = func(value)
    return total

print("Total bill: ", total_bill(add_tax, 100))

# если функция это объект, то мы сможем передавать его как аргумент функции

# filter
# filter(func, iterable)  --> filter object

def find_even(x):
    return x % 2 == 0

print(list(filter(lambda x : x % 2 == 0, numbers)))
print(list(filter(find_even, numbers)))
print(1 == 1)


# names=['Sa', 'Muhammad', 'Farina', 'Hanifa', 'Asmira', 'Bohir']

# фильтр, который записывает имена, длина которых больше или равно 3

# def long_names(x):
#     return len(x) >=3

# print(list(filter(lambda x: len(x) >= 3, names)))
# print(list(filter(long_names, names)))


# print(list(zip(numbers, numbers_2, numbers_3)))

# numbers={i:str(i) for i in range(10)}
# numbers_2={i:str(i) for i in range(10,15)}
# print(dict(zip(numbers.values(), numbers_2.values())))

from functools import reduce
def custom_sum(initial, num):
    print(initial, num)
    return initial - num


# reduce(function, iterable[, initial])
print(reduce(custom_sum, numbers))

