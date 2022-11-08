# For pools
name="Hello, world"
for i in name: 
  print(i)

name="Hello!!"
for i in range(1,6): # Я хочу чтобы код выводился 5 раз, поэтому пишу в скобках от 1,6,потому что 6 не включительно
    print(name)

name="world"
for i in name: 
  print(i)
  i='Hello'
  print(i)


print("числа от 1 до 20")
for i in range(1,21):  # число 20 не вкл.
  print(i)

print("число до 4")
for b in range(4): #выводятся числа до 4
  print(b)


print("получить значения в квадрате от 1 до 10")
for k in range (1,11): # чтобы получить значения в квадрате
  print(k,k**2)


# можем найти сумму всех чисел до  2
s=0
for l in range (1,3):  # 0+1 
  s=s+l
print(s)
#s=0+1 s=1, s=1+2, s=3



print("факториал числа 3!=1*2*3")# чтобы найти факториал от 3   произведение
pr=1  #(пишем 1, потому что если писать 0 то всё обнулиться)
for i in range(1,4):
  pr=pr*i
  print(pr)

# как найти факториал числа n
# print("факториал числа n!=1*2*...*(n-1)*n") 
# n=int(input())
# pr=1  #(пишем 1, потому что если писать 0 то всё обнулиться)
# for i in range(1, n+1):
#   pr=pr*i
#   print(pr)
print("вывод hello 6 раз")
for i in range (6):
  print('hello')


for i in [1,2,3,4,5,[1,2]]:
  print(i)