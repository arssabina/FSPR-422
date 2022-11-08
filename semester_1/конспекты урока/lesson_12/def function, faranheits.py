# if 1==1:
#     print(True)
# =======================================
# def greet():
#     print("Hello")
# # вызов функции
# print("вызов функции", greet()) 


# def greet():
#     return "Hi"

# result = greet()
# print(result)
# # =======================================


def greet(name): # name - это аргумент функции
    print(f"Hello {name}")

# greet ("Behruz")
# s= "Bekzod"
# greet (s) # "Bekzod"
greet(input("Input name:"))

# def greet(name):
#     return f"Hello {name}"

# print(greet("Jamshid"))
# result=greet ("Aybek")
# print(result)

# ====================================================================

# Задание: Написать функцию которая принимает список фаренгейтов и возвращает список цельсия

# faranheits = [30, 20, 19, 24, 45]  

# def fars_to_cels(faranheits):
#     result=[]
#     for far in faranheits: 
#         celsius = (far - 32) * 5 / 9
#         result.append(celsius)
#     return(result)
# print(fars_to_cels(faranheits))

# Задание-2: Перепистать код по рисованию квадрата с помощью функции def:

# n= 6 
# star = "*" 
# def draw_square(n,star):
#     for i in range(n):
#         if i>0 and i< (n-1): 
#             empty_space = " " * (n-2)
#             print(f"{star}{empty_space}{star}")
#         else: 
#             print(star*n)

# draw_square(10,"*")

