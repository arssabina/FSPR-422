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

# ===============================================================
# 7 kyu Square Every Digit  https://www.codewars.com/kata/546e2562b03326a88e000020/train/python
# Welcome. In this kata, you are asked to square every digit of a number and concatenate them.
# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.
# Note: The function accepts an integer and returns an integer

def square_digits(num):
    num_1=list(str(num))
    # print(num_1)
    result = []
    for i in num_1: 
        num_square=(int(i)**2)
        result.append(num_square)
    print(''.join(result))
    

square_digits(9119)