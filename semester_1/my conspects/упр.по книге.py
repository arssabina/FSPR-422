# magicians = ['alice', 'david', 'carolina'] 
# for magician in magicians: 
#     print(magician.title() + "," + "that was a great trick!!!")
#     # Так как обе команды print снабжены отступами, каждая строка будет выполнена по одному разу для каждого фокусника в списке
#     print("I can't wait to see your next trick, " + magician. title() + ".\n")

# ВЫвод::
# Alice,that was a great trick!!!
# I can't wait to see your next trick, Alice.

# David,that was a great trick!!!
# I can't wait to see your next trick, David.

# Carolina,that was a great trick!!!
# I can't wait to see your next trick, Carolina.

# pizzas=["peperroni", "cheese pizza", "kid's pizza"]
# # print(pizza)
# for pizza in pizzas:
#     print("I love " + pizza)
# print("I really love pizza")

# squares=[]
# for val in range(1,11):
#     squares.append(val**2)
# print(squares)                   # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# или
#  
# result=[]
# for val in range(1,11):
#     square=val**2
#     result.append(square)
# print(result)         # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# 

digits=[1,2,3,4,5,6,7,8,9,10]
print(sum(digits))