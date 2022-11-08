# 1-задание. Написать функцию по нахождению чисел фиббоначи
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711.....

def fib(n):
    fib_1=0
    fib_2=1
    for i in range(n):
        fib_1, fib_2 = fib_2, fib_1+fib_2
        print(fib_2, end=" ")
fib(10) # кол-во элементов ряда фибоначчи

# ============================================================================================================================
# 2-задание: Написать функцию, которая принимает список строк и из этого списка создает словарь,  
#     где ключами словаря являются значения списка, а значения словаря должны быть None. 

def my_list(*args):
    print("args=", args, type(args))
    for val in args:
        d=dict.fromkeys(val)
        print("d=", d, type(d))
my_list(["name", "age", "skill", "hobby"])

# =======================================================================================================================
# 5-задание: Написать функцию, которая создает список внутри списка с 3 столбцами и 4 строками (матрица).
def list_in_list(*args):
    print("[")
    for i in args:
        print("  ", i,",")
    print("]")
list_in_list([1,2,3],[1,2,3],[1,2,3],[1,2,3])

# # ============================================================================
my_list=[1,2,3],[1,2,3],[1,2,3],[1,2,3]
def matrix_1 (my_list):
    for i in my_list:
        print("   ", i)
matrix_1(my_list)

# ===============================================================================
matrix=[[0,1,2],
        [1,2,3],
        [4,5,6],
        [7,8,9]]
rows=len(matrix)   
columns=len(matrix[0])
print("[")  
for i in range(rows):
    print("  ", matrix[i])
print("]")
# ====================================================================================
# 4-задание: Решить эту задачу из кодварса (часть решения я показывал в классе)  
# def shades_of_grey(n):
#     shades=[]
#     hex="0123456789abcdef"
#     counter=0
#     for i in range(n): # n =20
#         if counter ==16:
#             counter=0
#         grey=f"#0{hex[counter]}0{hex[counter]}0{hex[counter]}"
#         if i >=16:
#             grey = f"#1{hex[counter]}1{hex[counter]}1{hex[counter]}"
#         if i >=32:
#             grey = f"#2{hex[counter]}2{hex[counter]}2{hex[counter]}"
#         if i >=48:
#             grey = f"#3{hex[counter]}3{hex[counter]}3{hex[counter]}"
#         if i >=64:
#             grey = f"#4{hex[counter]}4{hex[counter]}4{hex[counter]}"
#         if i >=80:
#             grey = f"#5{hex[counter]}5{hex[counter]}5{hex[counter]}"
#         if i >=96:
#             grey = f"#6{hex[counter]}6{hex[counter]}6{hex[counter]}"
#         if i >=112:
#             grey = f"#7{hex[counter]}7{hex[counter]}7{hex[counter]}"
#         if i >=128:
#             grey = f"#8{hex[counter]}8{hex[counter]}8{hex[counter]}"
#         if i >=144:
#             grey = f"#9{hex[counter]}9{hex[counter]}9{hex[counter]}"
#         if i >=160:
#             grey = f"#A{hex[counter]}A{hex[counter]}A{hex[counter]}"
#         if i >=176:
#             grey = f"#B{hex[counter]}B{hex[counter]}B{hex[counter]}"
#         if i >=192:
#             grey = f"#C{hex[counter]}C{hex[counter]}C{hex[counter]}"
#         if i >=208:
#             grey = f"#D{hex[counter]}D{hex[counter]}D{hex[counter]}"
#         if i >=224:
#             grey = f"#E{hex[counter]}E{hex[counter]}E{hex[counter]}"
#         if i >=240:
#             grey = f"#F{hex[counter]}F{hex[counter]}F{hex[counter]}"
        
#         shades.append(grey)
#         for val in shades: 
#             if val=='#000000':
#                 shades.pop(0)
#             # if val=='#555555':
#             #     shades.pop(0)
                
#         counter +=1
#     return shades

# print(shades_of_grey(255))

# ==================================================== ПРАВИЛЬНОЕ РЕШЕНИЕ: ======================================
# РЕШЕНИЕ ХУСАНА:

# def shades_of_grey(n):
#     shades = []
#     hex = '0123456789abcdef'
#     counter = 0
#     b = 0
#     if 0 <= n <= 254:
#         for i in range(n+1):
#             if counter ==  16:
#                 counter = 0
#                 b += 1
#             gray = f'#0{hex[counter]}0{hex[counter]}0{hex[counter]}'
#             if i == 16:
#                 gray = f'#{hex[b]}{hex[0]}{hex[b]}{hex[0]}{hex[b]}{hex[0]}'
#             if i >= 17:
#                 gray = f'#{hex[b]}{hex[counter]}{hex[b]}{hex[counter]}{hex[b]}{hex[counter]}'
#             shades.append(gray)

#             counter += 1
#     elif 254 <= n:
#         for i in range(255):
            
#             if counter ==  16:
#                 counter = 0
#                 b += 1
#             gray = f'#0{hex[counter]}0{hex[counter]}0{hex[counter]}'
#             if i == 16:
#                 gray = f'#{hex[b]}{hex[0]}{hex[b]}{hex[0]}{hex[b]}{hex[0]}'
#             if i >= 17 or i <= 256:
#                 gray = f'#{hex[b]}{hex[counter]}{hex[b]}{hex[counter]}{hex[b]}{hex[counter]}'
#             shades.append(gray)

#             counter += 1

#     if shades:
#         shades.pop(0)
#         return shades
#     elif n < 0:
#         return []
#     else:
#         return shades

# РЕШЕНИЕ УЧИТЕЛЯ: 
def shades_of_grey(n):
    shades=[]
    second_hex="0123456789abcdef"
    first_hex="0123456789abcdef"
    if n  < 0: 
        return shades
    counter=0
    for _ in range(n//10+1): # n =20
        if counter ==16:
            counter=0
        if (n+1) == len (shades) or len (shades) ==255:
                break
        for j in range(16):
            if (n+1) == len (shades) or len (shades) ==255:
                break
            print(j)
            grey=(f"#{first_hex[counter]}{second_hex[j]}"
                  f"{first_hex[counter]}{second_hex[j]}"
                  f"{first_hex[counter]}{second_hex[j]}")
            shades.append(grey)
        counter+=1
    
    if shades:  
        shades.pop(0)
    if len(shades) >=255:
        shades.pop(254)
    return shades

print(-2//10)
print(shades_of_grey(300))
          

