# Disemvowel Trolls
# Trolls are attacking your comment section!
# A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.
# Your task is to write a function that takes a string and return a new string with all vowels removed.
# For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
# Note: for this kata y isn't considered a vowel.
# https://www.codewars.com/kata/52fba66badcd10859f00097e

# def disemvowel(string_):
#     return string_

# def disemvowel(current_str):
#     new_str=[]
#     vowels=['a','o','e','i','u','A', 'O', 'E','I','U']
#     for letter in current_str:
#         if letter not in vowels:
#             new_str.append(letter)
#         else:
#             print("")
#     print("".join(new_str))

# disemvowel("hello, my happy world!")

# =================================================================================
# так легче: 
# 2-способ: Можно удалением всех гласных букв из списка методом replace:

# def disemvowel(message):
#     vowels=['a','o','e','i','u','A', 'O', 'E','I','U']
#     for vowel in vowels:
#         message=message.replace(vowel,"")
#     print(message)

# disemvowel("hello, I'm glad to see you!")

   
# def get_count(sentence):
#     count=0
#     vowels=['a','o','e','i','u']
#     vowel_y=['y', 'Y']
#     if sentence:
#         length=len(sentence)
#         if length==0:
#             print("len", 0)
#     for letter in sentence:
#         if letter in vowel_y:
#             print(0)
#         if letter not in vowels:
#             print(0)
#         if letter in vowels:
#             count=count+1
#     print("The number of vowels: ", count)
        
# get_count("hello, I'm glad to see you!")
 
# ====================================================================
  
# def get_count(sentence):
#     vowels='aeiou'
#     count=0
#     for letter in sentence:
#         if letter.lower() in vowels: 
#             count+=1
#     print("The number of vowels: ", count)

# get_count("abracadabra")
# ==========================================================================================
# vowelOne
# Write a function that takes a string and outputs a strings of 1's and 0's where vowels become 1's and non-vowels become 0's.
# All non-vowels including non alpha characters (spaces,commas etc.) should be included.
# Examples:
# vowelOne "abceios" -- "1001110"
# vowelOne "aeiou, abc" -- "1111100100"
# https://www.codewars.com/kata/580751a40b5a777a200000a1/train/python

# def vowel_one(s):
#     vowels='aeiou'
#     for letter in s:
#         if letter.lower() in vowels: 
#             s=s.replace(letter,"1")
#         else:
#             s=s.replace(letter,"0")
#     print(s)

# vowel_one("abceios")

# =========================================================
# Вывод наибольшего числа из списка! 
# def largest(n,xs):     # n = кол-во наибольш.чисел, кот.выводится в ответ,   xs = список с числами [2,4,58,99,78]
#     xs.sort()
#     print(xs[-n:])

# largest(5,[2,4,58,99,78])


# best code: ++++++++++++++++++++++++++++++++++
# def largest(n,xs): 
#     print(sorted(xs)[-n:])

# largest(5,[2,4,58,99,78])

# ===============================================
# FizzBuzz   https://www.codewars.com/kata/5300901726d12b80e8000498/train/python
# Return an array containing the numbers from 1 to N, where N is the parametered value.

# Replace certain values however if any of the following conditions are met:

# If the value is a multiple of 3: use the value "Fizz" instead
# If the value is a multiple of 5: use the value "Buzz" instead
# If the value is a multiple of 3 & 5: use the value "FizzBuzz" instead
# N will never be less than 1.

# Method calling example:

# fizzbuzz(3) -->  [1, 2, "Fizz"]

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
    
# =================================================================

# import math
# def solution(start, finish):
#         difference=finish-start
#         steps=math.floor(difference/3)+difference%3
          
#         print(steps)

# solution(2,4)
# ===================================================
# def solution(start, finish):
# #     if start: 
#             (print(2))
#     if start==2 and finish ==4: 
#             (print(2))
            

# def solution(start, finish):
#     difference=finish-start
#     steps=difference % 3
#     print(steps)


# solution(1,5)

# ==========================================================================
    # Highest and Lowest      https://www.codewars.com/kata/554b4ac871d6813a03000035/train/python
# you are given a string of space separated numbers, and have to return the highest and lowest number.

# def high_and_low(numbers):
#     numbers=numbers.split(" ")
#     numbers=sorted(numbers,key=int)
#     print(numbers[-1] + "  " + numbers[0])

# high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4")
   


