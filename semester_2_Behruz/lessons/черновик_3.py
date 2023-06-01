# Числа Фибоначчи (строка Фибоначчи) — числовая последовательность, первые два числа которой являются 0 и 1,
# а каждое последующее за ними число является суммой двух предыдущих
# def fib(n):
#     if n==1:
#         return 0
#     if n==2:
#         return 1
#     else: 
#         return fib(n-1)+fib(n-2)

# print(fib(3))


# def factorial():
#     for num in range(5):
#         if num == 0:             
#             return 1
#         else: 
#             yield num * factorial(n-1)

# f = factorial()
# print(list(f))

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