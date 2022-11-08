# 1-задание: Пробовала разные варианты, отправляю то-что есть(д.з.не поняла что надо было делать)

number=int(input("Введите число:"))
print((isinstance(number, int)), type(number))

name = input("Введите ваше имя:")
print((isinstance(name, str)), type(name))

names= input("Enter your data:").split() 
print((isinstance(names, list)), type(names))

data_1=set(input("Введите данные:"))
print((isinstance(data_1, set)), type(data_1))

кортеж = tuple(input(" Любая информация: "))
print((isinstance(кортеж, tuple)), type(кортеж))


# ============================================================================================================

# 2-задание: Принять через Input 3 значения: xp (int), damage (int), mp (int). Сравнить эти числа и если 
# xp<=100 damage<=10 mp<=50 -> "Уровень 1"
# xp<=300 damage<=20 mp<=100 -> "Уровень 10"
# xp<=500 damage<=100 mp<=200 -> "Уровень 15" 
# Если больше этого -> "Вы герой"

# 1-метод:
xp=int(input("xp:"))
damage=int(input("damage:"))
mp=int(input("mp:"))
print(xp,damage,mp)

if xp <= 100:
    print("Уровень 1")
elif xp <=300:
    print("Уровень 10") 
elif xp <=500:
    print("Уровень 15")
elif damage <=20:
    print("Уровень 1") 
elif damage <=20:
    print("Уровень 10") 
elif damage <=100:
    print("Уровень 15") 
elif mp <=50:
    print("Уровень 1") 
elif mp <=100:
    print("Уровень 10") 
elif mp <=200:
    print("Уровень 15") 
else:
    print("Вы герой")
    
# ============================================================================================================
# 2-метод:
xp=int(input("XP:"))
print(xp)

if xp <= 100:
    print("Уровень 1")
elif xp <=300:
    print("Уровень 10") 
elif xp <=500:
    print("Уровень 15")
else:
    print("Вы герой")

damage=int(input("Damage:"))
print(damage)

if damage <= 10:
    print("Уровень 1")
elif damage <=20:
    print("Уровень 10") 
elif damage <=100:
    print("Уровень 15")
else:
    print("Вы герой")

mp=int(input("MP:"))
print(mp)
if mp <=50:
    print("Уровень 1") 
elif mp <=100:
    print("Уровень 10") 
elif mp <=200:
    print("Уровень 15") 
else:
    print("Вы герой")

# print(isinstance("qwer", (int,str)))

# isinstance("qwer", (int,str))
print(type("qwerty"), str, "qwerty"

    
     