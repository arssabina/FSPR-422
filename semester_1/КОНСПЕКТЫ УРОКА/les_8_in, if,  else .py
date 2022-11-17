# in 
# s = {[2,3]} # множество может хранить только неизменяемые типы переменных 


print("in =", 1 in [2,3,4,1])
print("in =", "Hi" in "Hi me name is SMTH")  # True\ False
print("in =", [1,2] in [2,3,4, [1,2]])       # True\ False
print("in =", {1,2} in [2,3,4, {1,2}])       # True\ False

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


