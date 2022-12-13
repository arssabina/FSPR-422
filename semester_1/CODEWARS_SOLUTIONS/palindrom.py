# Числа-палиндромы — числа, которые в определённой позиционной системе исчисления (как правило — в десятичной) читаются 
# одинаково как справа налево, так и слева направо.

# def palindrom(n):
#     number=str(n)
#     test=number[::-1]
#     if number==test:
#         print("It's palindrom number")
#     else:
#         print("It's not palindrome number")

# palindrom(12)

# =====================================================================
# How to find next palindrome number   Мой вариант решения
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
# Better solution:

# def next_pal(val):
#     val += 1
#     while str(val) != str(val)[::-1]:
#         val += 1
#     print(val)

# next_pal(11)
