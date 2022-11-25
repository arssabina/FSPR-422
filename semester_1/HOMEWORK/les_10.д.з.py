# 1-задание: Создать программу которая записывает в список 2 словаря состоящий из двух ключей: "name" и "age"  
# и при этом используйте input и for 

# 1-метод:+++++++++++++++++++++++++++++++++++++++++++++++++

info=[]
for i in range(10):
    info.append(
    {
    "name": input("Enter your name:"),
    "age": int(input("Your age:"))
    }
)
print(info)

# 2- метод:++++++++++++++++++++++++++++++++++++++++++++++++++++
info=[]
for i in range(10):
    name= input("Enter your name:")
    age= int(input("Your age:"))
    info.append(
    {
        "age": age,
        "name": name,
    }
)
print(info)

# ==============================================================================================================
# 2 - задание: 
# Написать программу, которая переводит значение из списка из фарангейта в цельсий.  
# Если после перевода на цельсий градус выше 50, закончить цикл и вывести на экран "Слишком горячо" 
# Если ниже 5 вывести на экран "Жить можно"  
# Формула нахождения цельсия из фарангейта: (32F − 32) × 5/9 = 0C 

faranheits =[20,19,24,45,130,140]
celsius = [(faranheits[0]- 32) * 5 / 9, (faranheits[1]- 32)* 5 / 9, (faranheits[2]- 32) * 5 / 9, (faranheits[3]- 32) * 5 / 9,(faranheits[4]- 32) * 5 / 9,(faranheits[5]- 32) * 5 / 9]
print("celsius =", celsius, type(celsius))
for i in celsius:
    if i < 5.0:
        print("Жить можно")
        continue
    elif i > 50.0: 
        print ("Слишком горячо", "break")
        break


result=[]
faranheits =[20,140, 19,24,45]
for far in faranheits:
    celsius = (far- 32) * 5 / 9
    if celsius >=50:
        print ("Слишком горячо", "break")
        break
    elif celsius <= 5:
        print("Жить можно")
    result.append(celsius)
print(result)



# ==============================================================================================================
# Перевод значения фарангейта в цельсий через input
# faranheits = int(input("Введите градус фаренгейта: "))
# celsius = [int((faranheits- 32) * 5 / 9)]
# print("celsius =", celsius, type(celsius))
# for i in celsius:
#     if i < 5.0:
#         print("Жить можно")
#         continue
#     elif i > 50.0: 
#         print ("Слишком горячо")
#     else:   
#         print("Отлично")
    