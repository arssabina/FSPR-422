# Strange principal
# https://www.codewars.com/kata/55fc061cc4f485a39900001f/train/python
# test.assert_equals(num_of_open_lockers(56),7)
# test.assert_equals(num_of_open_lockers(128),11)

# def num_of_open_lockers(n):
#     import math
#     open_lockers=math.floor(math.sqrt(n))
#     print(open_lockers)

# num_of_open_lockers(128)

# ======================================================================
# https://www.codewars.com/kata/55fd2d567d94ac3bc9000064/train/python
# 1 -->  1
# 2 --> 3 + 5 = 8
# test.assert_equals(row_sum_odd_numbers(2), 8)
# test.assert_equals(row_sum_odd_numbers(13), 2197)
# test.assert_equals(row_sum_odd_numbers(19), 6859)
# test.assert_equals(row_sum_odd_numbers(41), 68921)

# def odd_row(n):
#     result=[]
#     start=n**2-(n-1)
#     result.append(start)
#     for i in range(n-1):
#         start+=2
#         result.append(start)
#     return (sum(result))
    
# print(odd_row(4))

# """"Самое лучшее решение:"""
# def row_sum_odd_numbers(n):
#     return n ** 3

# print(row_sum_odd_numbers(3))

# ===========================================================================================
# https://www.codewars.com/kata/54c27a33fb7da0db0100040e/train/python
# You're a square!

# def is_square(n):
#     import math
#     if n>=0:
#         square_number=math.sqrt(n)  # вычисляем корень числа 
#         check=square_number**2     # проверяем число, возводим в степень и проверяем  
#         if check==n:               # если возведенное число == числу n, True
#             return True
#         else: 
#             return False
#     else: return False

# print(is_square(-1)) 

# # -------------------------------------
# # Another solution: 

# def is_square(n):
#     import math
#     return n > -1 and math.sqrt(n) % 1 == 0

# print(is_square(25)) 


# https://www.codewars.com/kata/55f2b110f61eb01779000053/train/python
# def get_sum(a,b):
#     small, big = sorted([a,b])
#     if a == b:
#         return a
    
#     return sum([i for i in range(small, big +1)])
        
# print(get_sum(2, 3))

# def get_sum(a,b):
#     return sum(range(min(a,b), max (a,b) +1))

# print(get_sum(2,3))

# https://www.codewars.com/kata/5656b6906de340bd1b0000ac/train/python
# def longest(str_1, str_2):
#     s=set("".join([str_1, str_2]))
#     result="".join(sorted(s))
#     return result
    
# print(longest("aretheyhere", "yes"))

# Best solution:
# def longest(a,b):
#     return "".join(sorted(set(a + b)))

# print(longest("aretheyhere", "yes"))

# https://www.codewars.com/kata/55b42574ff091733d900002f/train/python
# def friend(x):
#     result=[]
#     for name in (x):
#         if len(name) == 4:
#             result.append(name)
#     return result
    
# print(friend(["Ryan", "Kieran", "Mark"]))

# # best solution
# def friend(x):
#     return [f for f in x if len(f) == 4]

# print(friend(["Ryan", "Kieran", "Mark"]))

# =====================================================================
# https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa/train/python/63b30bfcec7c3d0017e66d72
def open_or_senior(data):
    result=[]
    for age, handicap in (data):
        if age >= 55 and handicap >7:
            result.append("Senior")
        else:
            result.append("Open")
    return result

print(open_or_senior(([(45, 12),(55,21),(19, -2),(104, 20)])))


# def find_next_square(n):
#     import math
#     #  возведение в степень 0,5 это то же самое, что извлечь квадратный корень
#     # (144**0.5)=12 и    math.sqrt (144)=12 
#     if n % (n**0.5) == 0:
#         # или можно написать так: # if n % (sqrt(n)) == 0: 
#         return pow((math.sqrt(n)+1),2)  # or : return  (sqrt_1+1) **2     
#     else:
#         return -1 

# print(find_next_square(144))

# Best soultion
# def find_next_square(sq):
#     root = sq ** 0.5
#     if root.is_integer():
#         return (root + 1)**2
#     else:
#         return -1

# print(find_next_square(155))


# https://www.codewars.com/kata/563b662a59afc2b5120000c6/train/python

# def nb_year(p0, percent, aug, p):
#     count=0
#     while p0 < p:
#         count += 1
#         p0=p0 + int(p0*(percent/100)) + aug
#     return count
               
# print(nb_year(1500, 5, 100, 5000))


# def nb_year(p0, percent, aug, p, years = 0):
#     if p0 < p:
#         return nb_year(p0 + int(p0 * percent / 100) + aug, percent, aug, p, years + 1)
#     return years
