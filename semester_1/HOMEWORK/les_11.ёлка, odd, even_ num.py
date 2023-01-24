# Задание с сортировкой словарей:
# sort_dict({3:"hello", 2:"hello", 1:"hello"}) == [(1,"hello"), (2,"hello"), (3,"hello")] 
# sort_dict({1:2, 2:4, 3:6}) == [(3,6), (2,4), (1,2)]

# dict = {3:"hello", 2:"hello", 1:"hello"}
# d_1 = sorted(dict.items())
# print(d_1)

# dict = {3:"hello", 2:"hello", 1:"hello"}
# my_list=list(dict.items())
# my_list.sort()
# print(my_list)

# =====================================================================================
# 1-задание 
# Используя цикл вывести на экран ёлку 
#     * 
#    *** 
#   * 
#  *** 
#     * 
#     *
# n=10
# space=" "
# symbol="*"
# for i in range(n):
#     print(space * (n-i-1), symbol* (i*2+1)) # 1 - line: space: 10-0-1, symbol 0*2+1=1
# print(space*(n-1)+symbol)
# print(space*(n-1)+symbol)


# ==============================================================
# 2-задание: 
# Найти четные и нечетные числа в списке и вывести на экран сообщение что они четные или нечетные. с циклом for
# четные - 2 4 6 
# нечетные - 3 5 

# numbers=[2, 3, 4, 5, 6] 
# even=[]
# odd=[]
# for i in numbers:
#     if i % 2 == 0:
#         even.append(i)
#     else: 
#         odd.append(i)
# print("Чётные числа=", even, "Нечётные числа=", odd)


def even(a):
    if a%2 == 0:
        print("Четное число:", a)
    else: 
        print("Нечётное число:", a)
for i in range (20,31):
    even(i)


# ========================================================================================
# 3-задание: Переписать код перевода списка чисел из фарангейт в цельсий через while цикл. 

# result=[]
# faranheits = [20, 19, 24, 45, 140]
# i = 0
# while i < len(faranheits):
#     celsius = ((faranheits[i]) - 32) * 5 / 9
#     if celsius >= 50:
#         print("Слишком горячо")
#         break
#     elif celsius <= 5:
#         print("Жить можно")
#     print(celsius)
#     i += 1
# =========================================================================================
# 4-задание: 
# Переписать код по рисованию квадрата через while цикл.
# square_line = 6
# symbol = "*" 
# symbol_width = symbol * square_line
# i=0
# while i<square_line: #(чтобы он отработал столько раз, сколько написано в square_line)
#     if i>0 and i< (square_line-1): 
#         empty_space = " " * (square_line-2)
#         print(f"{symbol}{empty_space}{symbol}")
#     else: 
#         print(symbol*square_line)
#     i+=1   # на 6 линии i будет равен 6 и цикл while остановится (либо будет равен тому числу, которое указано в square _line)
