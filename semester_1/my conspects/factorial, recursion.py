# Факториал натурального числа n пишется как n! и считается как произведение всех натуральных
# чисел от 1 до n (включительно).

# Примеры:

# 1! = 1
# 2! = 1 ⋅ 2 = 2
# 3! = 1 ⋅ 2 ⋅ 3 = 6
# 4! = 1 ⋅ 2 ⋅ 3 ⋅4 = 24
# 5! = 1 ⋅ 2 ⋅ 3 ⋅ 4 ⋅ 5 = 120

# Формула факториала
# n!=1⋅2⋅3⋅...⋅(n−2)⋅(n−1)⋅n 

# def factorial(n):
#     if n==0:             
#         return 1
#     else: 
#         return n * factorial(n-1)

# print(factorial(5))

# def sum(n):
#     if n == 1:
#         return 1
#     else:
#         return n + sum (n-1)
# print(sum(3))


def fib(n):
    if n==1:
        return 0
    if n==2:
        return 1
    else: 
        return fib(n-1)+fib(n-2)

print(fib(5))