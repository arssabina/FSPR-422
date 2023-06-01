# #SCOPES - LEGB - области видимости

# # Local - локальная

# name="Farina"      # global

# def hello():
#     name="Sabina"   #locaL
#     print(name)

# hello()      

# print(name)     #global


# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []

# for x in fruits:
#   if "a" in x:
#     newlist.append(x)

# print(newlist)



def square(x): 
   return x**2

answer=list(map(square, [2,3,4,5,6]))
print(answer)

answer_2=list(map(lambda x : x **2))
print(answer_2)
