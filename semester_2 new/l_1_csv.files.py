# with open('doc.txt', 'r') as file:
#     lines = file.readlines()
#     for line in lines:
#         print(len(line))


# дз: напишите программу для записи содержимого списка в файл. каждый элемент в списке должен отображаться в файле с новой строки.
# список: 

colors = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

with open ('color_info.txt', 'w') as file: 
    for color in colors:
        file.write(color + '\n')
 