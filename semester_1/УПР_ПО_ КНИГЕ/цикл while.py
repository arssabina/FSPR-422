"""7-4. Дополнения для пиццы: напишите цикл, который предлагает пользователю вводить 
дополнения для пиццы до тех пор, пока не будет введено значение 'quit’. При вводе каждого дополнения
выведите сообщение о том, что это дополнение включено в заказ."""

# prompt="\nPlease enter toppings which would you like to your pizza:"
# prompt +="\n(Enter 'quit' when you are finished.) "

# while True:
#     pizza = input(prompt)

#     if pizza=='quit':
#         break
#     else: 
#         print(pizza + " included to your pizza") 

# responses={}
# polling_active = True
# while polling_active:
#     name = input("Please enter your name:")
#     response = input("Which mountain would you like to climb someday?")
#     responses [name] = response
#     repeat=input("Would you like to let another person respond? (yes/ no) ")
#     if repeat == "no":
#         polling_active = False
# print("\n===Polling results:===") 
# for name, response in responses.items():
#     print(name.title()  + " wants to climb " + response.title() + " someday")

"""УПРАЖНЕНИЯ
7-8. Сэндвичи: создайте список с именем sandwich_orders, заполните его названиями различных видов сэндвичей. 
Создайте пустой список с именем finished_sandwiches. В цикле переберите элементы первого списка и выведите 
сообщение для каждого элемента (например, «I made your tuna sandwich»). После этого каждый сэндвич из первого списка 
пермещается в список finished_sandwiches. После того как все элементы первого списка будут 
обработаны, выведите сообщение с перечислением всех изготовленных сэндвичей.
"""

# 7-8.

sandwich_orders=["roast beef sandwich","tuna sandwich", "hamburger", "sandwich", "sandwich monte-kristo"]
finished_sandwiches=[]
while sandwich_orders:
    made_sandwiches=sandwich_orders.pop()
    finished_sandwiches.append(made_sandwiches)
    print("I made your" +" " + made_sandwiches + "." )
print("\nI made:")
for sandwich in finished_sandwiches:
    print(sandwich.title())

# 7-9.Без пастрами: используя список sandwich_orders из упражнения 7-8, проследите за 
# тем, чтобы значение ‘pastrami’ встречалось в списке как минимум три раза. Добавьте в начало программы код для 
# вывода сообщения о том, что пастрами больше нет, и напишите цикл while для удаления всех вхождений
#  ‘pastrami’ из sandwich_orders. Убедитесь в том, что в finished_sandwiches значение ‘pastrami’ не встречается
#   ни одного раза.
sandwich_orders=["roast beef sandwich","pastrami", "tuna sandwich", "pastrami", "hamburger", "sandwich", "pastrami",
"sandwich monte-kristo"]
finished_sandwiches=[]
print("Sorry, our restaurant has run out of pastrami")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami") 
while sandwich_orders:
    made_sandwiches=sandwich_orders.pop()
    finished_sandwiches.append(made_sandwiches)
    print("I made your" +" " + made_sandwiches + "." )
print("\nI made:")
for sandwich in finished_sandwiches:
    print(sandwich.title())

"""
7-10. Отпуск мечты: напишите программу, которая опрашивает пользователей, где бы они 
хотели провести отпуск. Включите блок кода для вывода результатов опроса"""

dream_place=input ("Where would you like to spend your holiday?")
polling_active=True
while polling_active:
    print(dream_place + " nice place to spend your holiday!")
    response = input("Would you like to let another person respond? (yes/no)")
    if response == "no":
        polling_active = False
print("Thank you for taking our poll!")

    


