# ============================== УДАЛЕНИЕ ЭЛЕМЕНТОВ ИЗ СПИСКА МЕТОДОМ DEL   =================================
# bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# print(bicycles[0].title())
# message="Me favourite bicycle is " + bicycles[0].title() + "."
# print(message)
# del bicycles[1]
# print(bicycles)

# ==============УДАЛЕНИЕ ЭЛЕМЕНТОВ ИЗ СПИСКА====== DEL ======= POP ======== REMOVE  =================

# Разница между способом del и pop в том что, del полностью удаляет элемент, а после удаления элемента методом pop, удаленное из списка 
# значение остаётся доступным в программе
# Метод pop() удаляет последний элемент из списка, но позволяет работать с ним после удаления. 

# motorcycles = ['honda', 'yamaha', 'suzuki']
# popped_motorcycle = motorcycles.pop(0) 
# print(motorcycles)
# print(popped_motorcycle)

# # Если в скобках не писать номер индекса, pop удаляет последний элемент списка. 
# motorcycles = ['honda', 'yamaha', 'suzuki'] 
# last_owned = motorcycles.pop() 
# print("The last motorcycle I owned was a " + last_owned.title() + ".")
# # The last motorcycle I owned was a Suzuki.
# print(last_owned)

# names=['Ann', 'Jane', 'Peter']
# # removed_names=names.remove('Jane')   # в таком случае removed_names выдаёт None
# # print(removed_names)  # in this case removed_names gives None
# removed_name='Peter'
# names.remove(removed_name)
# print(names, removed_name)

# with 'remove' we can remove all occurences of an item in while loop:
# pets=['dog', 'cat', 'goldfish', 'cat', 'rabbit', 'cat']
# while 'cat' in pets:
#     pets.remove('cat')
# print(pets)


# ====================TO REMOVE ALL THE ELEMENTS OF THE LIST   =============== CLEAR================
# pets=['dog', 'cat', 'goldfish', 'cat', 'rabbit', 'cat']
# pets.clear()
# print(pets)

 
# ======================  REMOVE DUPLICATES  ==================================================
# To remove duplicates from a list we can create a dictionary, using the List items as keys.
# This will automatically remove any duplicates because dictionaries cannot have duplicate keys

# 1-method:

# pets=['dog', 'cat', 'goldfish', 'cat', 'rabbit', 'cat']
# pets=list(dict.fromkeys(pets))  
# print(pets)

# 2-method: to remove duplicates we can use set:
# pets=['dog', 'cat', 'goldfish', 'cat', 'rabbit', 'cat']
# pets=list(set(pets))
# print(pets)

b=[1,2,3,4,5,6,1,2,3,4, "AA", "BB", "AA"]
print(b, set(b), sep="\n")

print(b, list(set(b)), sep="\n")









