# Write a function which converts the input string to uppercase.
f=input("Enter your favourite fruit:")
print(f.upper())

f=input("Enter your favourite fruit:")
x=f.upper()
print(x)


def function (fruit=input("Enter your favourite fruit:")):
    print(fruit.upper())
function()

# ==========================================================================
# Написать функцию по возведению в числа степень. Вход: 2^4 - Ответ: 16

a=int(input("Число:"))
b=int(input("возвести в степень:"))
print("Ответ:", a**b)

a=int(input("Число:"))
b=int(input("возвести в степень:"))
c=pow(a,b)
print("Answer:",c)


def function(a=int(input("Введите число:")), b=int(input("возвести в степень:"))):
    print(a**b)
function()



