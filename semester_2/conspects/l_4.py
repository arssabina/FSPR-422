# import csv

# with open ('csv12_file', 'r') as file: 
#     csvreader = csv.reader(file) 
#     for row in csvreader:
#         print(row)

import csv
with open ('conspects\l4.csv', 'w', newline='') as file: 
    writer = csv.writer(file) 

    

    writer.writerow(["NO", "Player", "Record"])
    writer.writerow([1, "Sabina", "1202"])
    writer.writerow([2, "Farina", "1502"])
    writer.writerow([3, "Tamina", "0507"])
    
    name=input("Enter your name: ")
    age=input("Enter your age: ")
    last_name=input ("Enter your last_name: ")
    email=input("Enter your mail: ")
    while age.isdigit():
        info_about_me=[name, last_name, age, email]
        writer.writerow(info_about_me)
        file.close()



# row_list=[["Sabina", "Name", "Subject"], 
#             [1, "Farina", "English"],
#             [2, "Tamina", "Mathematics"],
#             [3, "Hanifa", "ARABIC"],
#             [4, "Asmira", "English"]]

# for val in row_list:
#     val == 'Mathematics':
#     ("Mathematics", "IT")
#     print(row_list)




