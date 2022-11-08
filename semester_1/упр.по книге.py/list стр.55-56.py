guests=['Ann', 'Jane', 'Peter', 'Tom']
message="Dear, " + guests[0] + ", " + " I want to invite you to my birthday party!" 
print(message)
                                                                   
guests.pop(2)
guests.append('Ella')
print(guests)

guests.insert(2, 'Helen')
print(guests)
guests.insert(3, 'Lizzy')
print(guests)

# to write an invitation to everybody from the last guests list
for i in (guests):
    message="Dear, " + i + "," + " I want to invite you to my birthday party!" 
    print(message)

# Используйте метод pop() для последовательного удаления гостей из списка до тех 
# пор, пока в списке не останутся только два человека. Каждый раз, когда из списка 
# удаляется очередное имя, выведите для этого человека сообщение о том, что вы сожалеете об отмене приглашения.

number_of_guests=(len(guests))  #общее кол-во гостей - 6
print(number_of_guests)  # 6 гостей
sorry_list=[]   
for i in range(number_of_guests-2):  # for цикл отработает 4 раза, чтобы осталось только два гостя
    popped_guests=guests.pop()      # сохраняем в переменной popped_guests отмененных гостей, 
                    # for цикл отработает 4 раза и удалить имена тех гостей которые находились в конце списка
    # print(popped_guests, end=" ")   #Ella Tom Lizzy Helen 
    sorry_list.append(popped_guests)  # в пустой лист (sorry_list) добавляем popped_guests 
    
print("Popped guests:", sorry_list)       # список людей, кому отправим сообщение с извинениями об отмене приглашения
print("Приглашенные гости:", guests)

for j in sorry_list:
    sorry_message= "Dear, " + j + "," + " I am so sorry, but today I can't invite you to my birthday party!"
    print("Sorry_messages:", sorry_message)
