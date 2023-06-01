my_file=open('test.txt ','r')
print(my_file.read())
print(my_file.readline())
print(repr(my_file.readline()))
my_file.close()
# =========================================

my_file=open('write.txt','w')
age=33
my_file.write(f'My name is Bekzod Age is {age}')
my_file.write(f'\nMy name is Samina Age is {age}')
my_file.close()
# =========================================
# context manager: _enter_- I __exit__

with open("test.txt", mode = 'r') as file:
    print(file.read()) 
    print(file.readline())  #читает одну строку
    print(file.readlines()) # читает все строки
    for row in file.readlines():
       print(row.strip()) # для того чтобы удалить отступы, используем strip
# =========================================
# # аналог кода with 

# Также можно написать try/finally, которое гарантирует, 
# что если после открытия файла операции с ним приводят к исключениям, он закроется автоматически.

try:
    my_file = open('write.txt', 'a')
    # code
except Exception as err: 
    print(err)
finally:
    my_file.close()


"""
read() - используется для чтения содержимого файла после открытия его в режиме чтения (r)
==================

readline() - используется для построчного чтения содержимого файла. Она используется для крупных файлов.
С ее помощью можно получать доступ к любой строке в любой момент.

x = open('test.txt','r')

x.readline()  # прочитать первую строку  O: This is line1.
x.readline(2)  # прочитать вторую строку O: This is line2.
x.readlines()  # прочитать все строки O: ['This is line1.','This is line2.','This is line3.']
===========
write() - используется для записи в файлы Python, открытые в режиме записи.
Если пытаться открыть файл, которого не существует, в этом режиме, тогда будет создан новый.

f = open('xyz.txt','w')  # открытие в режиме записи
f.write('Hello \n World')  # запись Hello World в файл 
f.close()   

"""

with open('test.txt', mode = 'w') as file:
    file.write(f'Some random data!')
with open ('test.txt', mode = 'a') as file: 
    for i in range(10):
        file.write(f'/nSome random data! {i}')


# import csv
# with open ('addresses.csv', newline ='') as addresses_csv:
#     address_reader = csv.DictReader(addresses_csv, delimiter=',')
#     # name: address; telephone
#     for row in address_reader:
#         print(row['Address'])


# import csv
# with open ('addresses.csv', newline ='') as addresses_csv:
#     address_reader = csv.DictReader(addresses_csv, delimiter=',')
#     # name: address; telephone
#     for row in address_reader:
        # if row['Name'] == 'Jennifer Barnett':           # для вывода инфо конкретного пользователя
            # print(row['Address'])


# with open("output.csv", 'w',  newline ='', encoding ='utf-8') as output_csv: 
#     fields = ['name', 'userid', 'is_admin']
#     # instantiate
#     output_writer = csv.DictWriter(output_csv, fieldnames=fields)
#     # write headers
#     output_writer.writeheader()
#     for item in big_list: 
#         output_writer.writerow(item)


big_list = [
    {'name': 'Sabina Arshidinova', 'user_id': 2457842, 'hobby': 'reading'},
    {'name': 'Asmira Arshidinova', 'user_id': 4789942, 'hobby': 'dancing'},
    {'name': 'Samir Arshidinov', 'user_id': 98762342, 'hobby': 'reading'},
    {'name': 'Sanjar Arshidinov', 'user_id': 111116992, 'hobby': 'reading'},

]

import csv
with open ('new_table.csv', 'w', newline='', encoding ='utf-8') as new_table_csv:
    fields = ['name', 'user_id', 'hobby']
    new_table_writer = csv.DictWriter(new_table_csv, fieldnames=fields)
    new_table_writer.writeheader()
    for item in big_list: 
        new_table_writer.writerow(item)