# 1- задание
login=input("Введите свой логин:")
print(login)

age=int(input("Введите свой возраст: "))
print(age)

if age < 18:
   print("Мы не можем зарегистрировать твой аккаунт! Тебе нет 18!")
else:
    print("Регистрация прошла успешно!")

# 2-задание

# 1-способ
a,b=input("(+)").split()
a=int(a)
b=int(b)
print(a+b)

a,b=input("(*)").split()
a=int(a)
b=int(b)
print(a*b)

a,b=input("(-)").split()
a=int(a)
b=int(b)
print(a-b)

a,b=input("(/)").split()
a=float(a)
b=float(b)
print(a/b)

a,b=input("(//)").split()
a=int(a)
b=int(b)
print(a/b)

a,b=input("(**)").split()
a=int(a)
b=int(b)
print(a**b)

# 2-способ

a,b=map(int,input("(+)").split())
print(a+b)

a,b=map(int,input("(-)").split())
print(a-b)

a,b=map(int,input("(*)").split())
print(a*b)

a,b=map(int,input("(/)").split())
print(a/b)

a,b=map(int,input("(**)").split())
print(a**b)
