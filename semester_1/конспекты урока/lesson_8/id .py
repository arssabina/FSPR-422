
# is, ==    сравнивает ID ДВУХ ЗНАЧЕНИЙ
# ID у изменяемых типов данных всегда уникальны. 
# ID у неизменяемых типов данных всегда одинаковые. 

a=1
b=1
print(id(a), id(b))

t_1= ()
t_2= ()
print(id(t_1), id(t_2))

print(t_1 == t_2)
print("tuple", t_1 == t_2)   # False
print("1==1", 1==1, 1 is 1)


# Изменяемые типы данных
#  []  []
l_1 = [1,2]   # 123456
l_2 = [1,2]   # 789415
print(l_1 ==1_2)
print(l_1 is l_2)

d_1 = {1:1}
d_2 = {1:1}
print("dict", d_1 == d_2)
print("dict", d_1 is d_2)

# print(l_1, is(l_1), l_2, id(l_2))

# l_1.append(4)
# print(l_1, is(l_1), l_2, id(l_2))


# ID у изменяемых типов данных всегда уникальны. 

# ID у неизменяемых типов данных всегда одинаковые. 


name= "Behruz"
skill = "D0"
age= 20
surname: "Saidjonov"

if name == "Sardor" and skill == "D2":  
    print(name,skill)
else:
    print("AND")

if name == "Sardor" or skill == "D2":  
    print(name,skill)
else:
    print("OR")

if not age:        # not - -> False True        not переводит true -> false, false->true
    print(age)
else:
    print("age is false")


             # True
     # True              True             True
if (name =="Behruz" and age > 18) or skill == "D2":
    print(name, age, skill)
else: 
    print("Invalid name, age, skill") 

   # True               false             true
if name=="Behruz" or age > 22 or skill == "D2":
    print(name, age, skill, "second output")
else: 
    print("Invalid name, age, skill") 


# Bool
# True\ False
# Любое число что не ноль - это правда (True)
# если переменная пустая - то она ложь (False)

# True = 1     False = 0

print(False * 3 )     # ответ   0
x = 10
y =20
if x>20:
    print(True)
else: 
    print(False)

# "name surname".split()   # Вывод: ['name, 'surname']
# a if condition else b
# print(True if x > y else False)


# ==, !=, >, >=, <, <=, is, is not, in, not in, not, and, or

# {}, [], " ", 0  - это всегда False  пустая строка, пустой список, 0 это всегда False


if []: 
    print(True)

if -19:
    print(True)  # выйдет True, потому что это не 0


