import csv
import json


# создать список compromised_users
# 1. Вывести на экран имена всех пользователей из файла passwords.csv и записать их в список compromised_users  

# passwords_list = [
#     {'name': 'Sabina Arshidinova', 'password': 123456},
# ]

# Create file passwords.csv with info about users and passwords

# with open ('password.csv', 'w', newline='', encoding ='utf-8') as passwords_csv:
#     fields = ['name', 'password']
#     passwords_writer = csv.DictWriter(passwords_csv, fieldnames=fields)
#     passwords_writer.writeheader()
#     for item in passwords_list: 
#         passwords_writer.writerow(item)


# ДОБАВЛЕНИЕ НОВЫХ СТРОК В СУЩ.ФАЙЛ 

# new_passwords_list = [
#     {'name': 'Helen', 'password': 54698941},
#     {'name': 'Ann', 'password': 6998844}, 
#     {'name': 'Jane', 'password': 63332114},
# ]

# with open("password.csv", 'a', newline='', encoding='utf-8') as file:
#     fields = ['name', 'password']
#     writer = csv.DictWriter(file, fieldnames = fields)
#     writer.writerows(new_passwords_list)

# ВЫВОД ВСЕХ ПОЛЬЗОВАТЕЛЕЙ passwords_csv:
# compromised_users = []
# with open('password.csv', 'r', newline='', encoding='utf-8') as file:
#     password_reader = csv.DictReader(file, delimiter=",")
#     for row in password_reader:
#         compromised_users.append(row)
#         print(row)


# print("Compromised users: ", compromised_users)
# ==================================================

# 2. Запись в compromised_users.txt файл данные из списка compromised_users 

# with open('compromised_users.txt', 'w', encoding = 'utf-8') as file:
#     for dict in compromised_users: 
#         for key, val in dict.items(): 
#             file.write('%s : %s\n' % (key, val))


# ==============================

# 3. Записать в файл boss_message.json словарь в json формате
# boss_message_dict = {
#     "recipient": "The Boss",
#     "message": "Mission Success",
# }

# # IMPORT TO json
# with open('boss_message.json', 'w') as json_file:
#     json.dump(boss_message_dict, json_file) 

# ========================================
# # 4. Записать в new_passwords.csv данную строку
# import csv            
# with open('names.csv', 'w', newline='', encoding='utf-8') as csvfile:
#     message_writer = csv.writer(csvfile, delimiter=' ')
#     message_writer.writerow(['''
#  _  _     ___   __  ____             
# / )( \   / __) /  \(_  _)            
# ) \/ (  ( (_ \(  O ) )(              
# \____/   \___/ \__/ (__)             
#  _  _   __    ___  __ _  ____  ____  
# / )( \ / _\  / __)(  / )(  __)(    \ 
# ) __ (/    \( (__  )  (  ) _)  ) D ( 
# \_)(_/\_/\_/ \___)(__\_)(____)(____/ 
#         ____  __     __   ____  _  _ 
#  ___   / ___)(  )   / _\ / ___)/ )( \
# (___)  \___ \/ (_/\/    \\___ \) __ (
#        (____/\____/\_/\_/(____/\_)(_/
#  __ _  _  _  __    __                
# (  ( \/ )( \(  )  (  )               
# /    /) \/ (/ (_/\/ (_/\             
# \_)__)\____/\____/\____/'''])

# 2 - Переписать использование констант Users и Products в классе из 27 урока первого семестра используя файлы

