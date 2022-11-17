# scope   LEGB rule  
# local enclosed global built-in 


print(print) # built-in

# Любой объект
name="Behruz"  # global

def get_name():
    name="George"  # local
    print(name)           # здесь будет локальный поиск
    
get_name()
# ====================================================================================

def get_name():
    name="Guido"  
   
get_name()
print(name)  # если написать print в этой строке, он идёт по глобальному поиску

# =======================================================================
# Глобальная
name="Dave"

def spam():
    name="Guido"  # ЛОкальная

spam
print(name)   # глобальная

# ========================================================================
name="Dave"
def spam():
    global name  # импортируем глобальную переменнную
    name="Guido"  # chandeg the global name above

spam
print(name)   # глобальная




def foo(items):
    items.append(42)

a=[1,2,3,4,5,6,7,8,9,10]
foo (a)
print(a)

a=[2,3]
b=a
b.append(2)
t_1=[1]       # id t_1 
t_2=[1]   
print(t_1 is t_2)

def bar (items): 
    items=[4,5,6]

b=[1,2,3]   # здесь мы изменили b, прервали связь между переменной a
bar(b)
print("b не поменялось", b)    # [1,2,3]

a=[1,2,3]
b=a
b=[2,4]
b.append(43)
print(a,b)


def parent():
    a=5
    return a
print("не вложенный", parent())  # 5 , здесь локальный поиск


def parent():
    a=5
    def answer():
        return a 
    return answer()
print("вложенный", parent())  # 5 , здесь enclosed поиск, он ищет не локальный, а enclosed поиск
# после того как он не находит в answer он идёт дальше наверх ищет там, потому что он вложенный
# enclosed работает только тогда если есть фукнция внутри функции



# global
a=20
def parent():
    # enclosed
    a=5
    def answer (): 
        # local
        a=10
        def get():
            return a 
        return get()
    return answer()


def outer():
    # enclosed
    x='local'

    def inner():
        # local
        nonlocal x    # nonlocal импортирует переменную с уровня enclosed, если не находит в enclosed выдаёт ошибку
        x='non local'
        print('inner:', x)
        
    inner()
    print('outer:', x)

outer()


name="Dave"
def spam():
    global name # импортируем глобальную переменную
    name = "Guido"   # импортирует глобальную переменную и изменяет её

spam()
print(name)