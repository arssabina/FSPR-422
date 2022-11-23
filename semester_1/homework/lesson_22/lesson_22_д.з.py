# How to find next palindrome number   Мой вариант решения 
# https://www.codewars.com/kata/56a6ce697c05fb4667000029/train/python
# def palindrom(n):
#     n=n+1
#     while True:
#         n=str(n)        # переводим номер в строку 
#         number=n[::-1]  # переворачиваем номер 
#         if n==number:       
#             print(int(n))
#             break
#         else: 
#             n=int(n)
#             n=n+1

# palindrom(33)

# ============================================================
# https://www.codewars.com/kata/5174a4c0f2769dd8b1000003/solutions/python
# Sort numbers: Finish the solution so that it sorts the passed in array of numbers. 
# If the function passes in an empty array or null/nil value then it should return an empty array.

def solution(nums):
    if nums:
        print(sorted(nums))
    else:
        print([])

solution([1,2,5,8,99])