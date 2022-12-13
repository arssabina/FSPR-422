# in проверяет, есть ли значение или переменная в последовательности
#  (строке, списке, кортеже, множестве или словаре). Иначе говоря, проверяют вхождение элемента в коллекцию.

# s = {[2,3]} # множество может хранить только неизменяемые типы переменных 


print("111in =", 1 in [2,3,4,1])   #True
print("222in =", "Hi" in "Hi me name is SMTH")  # True
print("333in =", [1,2] in [2,3,4, [1,2]])       # True
print("444in =", {1,2} in [2,3,4, {1,2}])       # True

if 1: 
    print(True)
else: 
    print(False)

if 0: # False 7n
    print(True)
elif 2==2:  # True
    print("elif 1")
elif 2==2:  # True
    print("elif 1")
elif 2==2:  # True
    print("elif 1")
else: 
    print(False)


name=12
print(isinstance(name, str))  # False

name_1=12
print(isinstance(name_1, int)) # True


b=True
print(type(b) == bool)   #True

b=True
print(type(b) ==int)   # False


