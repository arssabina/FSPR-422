# Теория
# 1. Назовите все типы переменных и их особенности:
# Изменяемые типы переменных: set, dict, list 
# значения этих типов переменных можно изменить
# Неизменяемые типы переменных: bin, frozenset, tuple, int, float, str, bool
# значения этих типов переменных нельзя изменить

# 2. Какие типы переменных можно хранить в качестве значений множества и ключа словаря. 
# В качестве значений множества и ключа словаря можно использовать только неизменяемые типы переменных:
# bin, frozenset, tuple, int, float, str, bool

# 3. Что такое MRO и наследование в питоне
# Наследование - это когда один класс наследует все атрибуты и методы другого класса. 
# Эта возможность передавать методы и данные одного класса другому классу. 
# MRO - Nethod Resolution Order - Порядок разрешения методов. Показывает цепочку наследования. 
# Этот метод позволяет узнать с какого-класса нужно вызывать метод. Очень полезный метод при множественном наследии.

# 4. Опишите процесс публикования изменений в гитхаб 
# После изменений: git status (Проверить текущий статус)-> git add . (подготовить файлы к git commit у, 
# сохранить все изменения) -> git status (Проверить текущий статус) -> - git commit -m "New commit" (Создание нового 
# коммита) -> git push (опубликовать все изменения)

# 5. В чем разница между функцией и методом?
# Функция - это подпрограмма, которая выполняет какие-то функции и возвращает значение.
# Метод - это функция, которая относится к классу или к экземпляру класса. Метод привязан к классу,
# а функция может работать в любой части программы

# ================================================================
# Теория + Задачи
# 1. Перечислите и Приведите пример оператов: сравнения, логических, особые операторы 
# Операторы сравнения:
# оператор < «меньше»
# оператор <= «меньше или равно
# оператор == «равно»
# оператор != «не равно»
# оператор > «больше»
# оператор >= «больше или равно»

# Логические операторы: or(или), and(и), not(не)
# Особые операторы: in - проверяет, есть ли значение или переменная в последовательности
#  (строке, списке, кортеже, множестве или словаре). Иначе говоря, проверяют вхождение элемента в коллекцию
# not in - проверяет, не находится ли значение или переменная последовательности
# is - сравнивает ID ДВУХ ЗНАЧЕНИЙ
# == используется для сравнения, car=='bmw' (проверяет равно ли значение car строке 'bmw' или нет). 
# = — для присваивания значения  car='bmw'  (присваивает переменной car значение bmw)

# 2. Что такое полиморфизм? приведите пример с полиморфизмом (надо создать свой пример)
# Полиморфизм - это способность объекта принимать множество форм. Частым примером полиморфизма служит наследие класса. 
class Pen: 
    def __init__(self, name, color):
        self.name=name
        self.color=color

    def info(self):
        print(f"This is a pen. It is {self.name}. It's ink color is {self.color}")

class Pencil: 
    def __init__(self, name, color):
        self.name=name
        self.color=color

    def info(self):
        print(f"This is a pencil. It is {self.name}. It's color is {self.color}")
   

pen=Pen("Penn", "blue")
pencil=Pencil("Pennncil", "black")

for thing in (pen, pencil):
    thing.info()
# # 
# 3. Исправьте код. В конце вы должны создать код по проверке данных ползователя и возвращает сообщение об успешном или
#  проваленном логине.
# ```py

def validate(username, password):
    if username == "Random" and password == "2321ewfsef":
        return f"Вы успешно вошли в систему!"
    else: 
        return f"Пароль имя пользователя не правильны"
    
print(validate("Random",'2321ewfsef'))

# ```
# 4. Приведете список областей видимости в питоне и пример с каждым из них.
# local enclosed global built-in
# в питоне есть 4 области видимости: локальная, enclosed, глобальная и встроенная

# 5. Описать что такое рекурсия и пример с нахождением чисел фиббоначи.
# Рекурсия - эта функция, которая вызывает сама себя. 
def fibonacci(fib_num):
    if fib_num in (1,2):
        return 1
    return fibonacci(fib_num-1) + fibonacci(fib_num-2)

### Задачи
# 1. Исправьте код ниже. После исправления код должен возваращть все аргументы, которые были приняты в виде
#  списка `other_info` и выводить их на экран: # ```py

def get_data(code, salary, *args, **kwargs):
    other_info = []
    for arg in args:
        other_info.append(arg)
        print(arg)
        for key, val in kwargs.items():
            other_info.append((key, val))
            return other_info

print(get_data(12, 1250, 29, 36, skills="Swimming"))
# ```  
# 2. Создать класс Gum, который описывает жевачку с атрибутами: smell, price, company, name, special_features, count и
#  с методом __str__, который возвращает информацию о жевачке со всеми атрибутами. 
# От класса Gum создать два других класса: Orbit и Trident. Orbit должен иметь ещё один атрибут country 
# (страна произвдства). Trident должен иметь ещё один атрибут date_of_production (дата производства).
# ```
# taste - вкус
# price - цена
# company - производившая компания 
# name - имя 
# special_features - имеет вкус арбуза, лимона и т.д.
# count - количество в упаковке
# # ```

class Gum:

    def __init__(self,name, smell, price, company, special_features, count):
        self.name=name
        self.smell=smell
        self.price=price
        self.company=company
        self.special_features=special_features
        self.count=count
    
    def __str__(self):
        return f"Class info: name={self.name}, smell={self.smell}, price={self.price}, company={self.company}, special_features={self.special_features}, count ={self.count}"


class Orbit(Gum):

    def __init__(self, name, smell, price, company, special_features, count, country):
        super().__init__(name, smell, price, company, special_features, count)  
        self.country=country


class Trident(Gum):

    def __init__(self, name, smell, price, company, special_features, count, date_of_production):
        super().__init__(name, smell, price, company, special_features, count)  
        self.date_of_production=date_of_production

gum=Gum("BEST Gum", "Mint",5000, "Gum company", "fresh and clean", 10)
print(gum)
orbit=Orbit("Orbit", "Fresh mint", 4000, "Orbit company", "clean teeth and fresh breath", 12, "Russia")
print(orbit)
trident=Trident("Trident", "Fruit mix", 20000, "Trident company", "enjoy gum", 8, 2021)
print(trident)


# 3. Вам даны два списка с значениями, которые являются силой каждого солдата. Верните True, если вы выжили атаку,
#  False, если проиграли. 
# **Условия**:
# - Каждый солдат атакует солдата противника с тем же индексом массива. Выживший - это число с наибольшим значением.
#     - Если значение одинаковое, они оба погибают
#     - Если одно из значений пусто (различная длина массива), солдат с непустым значением выживает.
# - Чтобы выжить, обороняющаяся сторона должна иметь больше выживших, чем атакующая сторона.
# - В случае, если с обеих сторон одинаковое количество выживших, побеждает команда с наибольшей начальной силой атаки. Если общая сила атаки обеих сторон одинакова, верните true.
#     - Начальная сила атаки представляет собой сумму всех значений в каждом массиве.
# ```
# attackers=[ 1, 3, 5, 7 ]   defenders=[ 2, 4, 6, 8 ]  
# //0 survivors                4 survivors
# //return true

# attackers=[ 1, 3, 5, 7 ]   defenders=[ 2, 4 ]  
# //2 survivors  (16 damage)   2 survivors (6 damage)
# //return false

# attackers=[ 1, 3, 5, 7 ]   defenders=[ 2, 4, 0, 8 ]  
# //1 survivors                3 survivors 
# //return true
# https://www.codewars.com/kata/634d0f7c562caa0016debac5
# ```
