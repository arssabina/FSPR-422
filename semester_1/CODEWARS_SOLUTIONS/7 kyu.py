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
#     numbers=numbers.split(" ")   # ['8', '3', '-5', '42', '-1', '0', '0', '-9', '4', '7', '4', '-4']
#     numbers=sorted(numbers,key=int)   # ['-9', '-5', '-4', '-1', '0', '0', '3', '4', '4', '7', '8', '42']
#     print(numbers[-1] + "  " + numbers[0])  # 42  -9
    
# high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4")


# ====================================================================================
# def largest(n,xs):     # n = кол-во наибольш.чисел, кот.выводится в ответ,   xs = список с числами [2,4,58,99,78]
#     xs.sort()  # Output -> [1, 2, 3, 4, 5, 6, 7]
#     print(xs[-n:])   # Output ->  [6, 7] 

# largest(2, [7,6,5,4,3,2,1])
    
# ====================================================================================
# Disemvowel Trolls
#
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

#  =====================================================================================  
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
# best code: ++++++++++++++++++++++++++++++++++
# def largest(n,xs): 
#     print(sorted(xs)[-n:])

# largest(5,[2,4,58,99,78])

##  =================================================================
# Cats and shelves
# https://www.codewars.com/kata/62c93765cef6f10030dfa92b/train/python/636f56dd2aae8f11e1a33fd6
#  import math
# def solution(start, finish):
#         difference=finish-start
#         steps=math.floor(difference/3)+difference%3
          
#         print(steps)

# solution(2,4)
#
# ===============================================================
# 7 kyu Square Every Digit  https://www.codewars.com/kata/546e2562b03326a88e000020/train/python
# Welcome. In this kata, you are asked to square every digit of a number and concatenate them.
# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.
# Note: The function accepts an integer and returns an integer

# def square_digits(num):
#     result=[]
#     for num in str(num):  
#         result.append(str(int(num)**2))          # Output -> ['81', '1', '1', '81']
#     final_result=(int(''.join(result)))      # Output -> 811181
#     print(final_result)

# square_digits(9119)


# ===========================================================================================
# Descending Order 
# https://www.codewars.com/kata/5467e4d82edf8bbf40000155/train/python
# Input: 42145 Output: 54421    переставьте цифры, чтобы получить максимально возможное число.

# def descending_order(num):
#     num_list=list(str(num))         # output -> ['4', '2', '1', '4', '5']
#     num_list.sort(reverse=True)     # output -> ['5', '4', '4', '2', '1']
#     result=int(''.join(num_list))   # output -> 54421
#     print(result)
    
# descending_order(42145)   
# 
# # best solution ->  

# def Descending_Order(num):
#     return int("".join(sorted(str(num), reverse=True))) 
# =============================================================================================
# Get the Middle Character
# https://www.codewars.com/kata/56747fd5cb988479af000028/train/python

# def get_middle(s):
#     if len(s) % 2 == 0:
#               #  s[2] + s[3]  для вывода средних букв, если кол-во букв = чётное число
#         print(s[(len(s)//2-1)]+s[(len(s)//2)])  
#     else: 
#         print(s[(len(s)//2)])   # для вывода средней буквы, если кол-во букв = нечётное число 
#              # output: dd
# get_middle("middle")

# ================================================================================
# Mumbling        https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/python
def accum(s):
    result=[]
    for n, letter in enumerate(s):
        # 0 R
        # 1 q
        # 2 a
        # 3 E 
        # 4 z
        # 5 t
        # 6 y
        print(n, letter)
        result.append(letter.upper()+letter.lower()*n)  # ['R', 'Qq', 'Aaa', 'Eeee', 'Zzzzz', 'Tttttt', 'Yyyyyyy']
    print("-".join(result))    # R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy    

accum("RqaEzty")

# +==============================================================================
#  https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/python
# Изограмма — это слово, в котором нет повторяющихся букв, последовательных или непоследовательных.
# Реализуйте функцию, определяющую, является ли строка, содержащая только буквы, изограммой
# isIsogram "Dermatoglyphics" = true
# isIsogram "moose" = false
# isIsogram "aba" = false 

# def is_isogram(s):
#     set_s=set(s.lower())     # {'e', 'o', 'h', 'l'}
#     if len(set_s)==len(s):   # 4 не равно 5   {'e', 'o', 'h', 'l'} не равно "Hello"
#        print (True)
#     else: 
#         print(False)
    
# is_isogram("Hello")
               
# =======================================================================

# https://www.codewars.com/kata/55f8a9c06c018a0d6e000132

# def validate_pin(pin):
#     if len (pin)==4 or len(pin)==6:
#         return pin.isdigit()
#     else: 
#         return False
    
# print(validate_pin("-12234"))


# def validate_pin(pin):
#     return len(pin) in (4, 6) and pin.isdigit()

# print(validate_pin("a2234"))

# https://www.codewars.com/kata/564e7fc20f0b53eb02000106/train/python

def consonant_count(s):
    vowels=['a','o','e','i','u','A', 'O', 'E','I','U']
    count=0
    for letter in s:
        if letter.isalpha() and letter not in vowels:
            count+=1
    return count
 
print(consonant_count("XaeiouX"))

def consonant_count(s):
    vowels='aoeiu'
    count=0
    for letter in s.lower():
        if letter.isalpha() and letter not in vowels:
            count+=1
    return count
 
print(consonant_count("Xa153poeiouX"))