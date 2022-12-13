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

def is_square(n):
    import math
    if n>=0:
        square_number=math.sqrt(n)  # вычисляем корень числа 
        check=square_number**2     # проверяем число, возводим в степень и проверяем  
        if check==n:               # если возведенное число == числу n, True
            return True
        else: 
            return False
    else: return False

print(is_square(-1)) 

# -------------------------------------
# Another solution: 

def is_square(n):
    import math
    return n > -1 and math.sqrt(n) % 1 == 0

print(is_square(25)) 
