# FizzBuzz   https://www.codewars.com/kata/5300901726d12b80e8000498/train/python
# Return an array containing the numbers from 1 to N, where N is the parametered value.

# Replace certain values however if any of the following conditions are met:

# If the value is a multiple of 3: use the value "Fizz" instead
# If the value is a multiple of 5: use the value "Buzz" instead
# If the value is a multiple of 3 & 5: use the value "FizzBuzz" instead
# N will never be less than 1.

# Method calling example: # fizzbuzz(3) -->  [1, 2, "Fizz"]

# def fizzbuzz(n):
#     result=[]
#     for num in range(1,n+1):
#         # print(num)
#         if num % 3 ==0 and num % 5== 0:
#             result.append("FizzBuzz")
#         elif num % 3 == 0:
#             # print("Fizz")
#             result.append("Fizz")
#         elif num % 5 == 0:
#             # print("Buzz")
#             result.append("Buzz")
#         else:
#             # print(num)
#             result.append(num)
#     print(result)

# fizzbuzz(10)


# ==========================================================================
    # Highest and Lowest      https://www.codewars.com/kata/554b4ac871d6813a03000035/train/python
# you are given a string of space separated numbers, and have to return the highest and lowest number.

# def high_and_low(numbers):
#     numbers=numbers.split(" ")
#     numbers=sorted(numbers,key=int)
#     print(numbers[-1] + "  " + numbers[0])

# high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4")


# ====================================================================================
def largest(n,xs):     # n = кол-во наибольш.чисел, кот.выводится в ответ,   xs = список с числами [2,4,58,99,78]
    xs.sort()
    print(xs[-n:])

largest(5,[2,4,58,99,78])
    