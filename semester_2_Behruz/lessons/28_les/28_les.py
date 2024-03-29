# паттерны в  Regex играет важную роль  
# regex101.com

# Этот модуль предоставляет операции сопоставления регулярных выражений в Python
# Основная функция модуля re — предложить поиск, в котором используются регулярное выражение и строка. 
# Здесь он либо возвращает первое совпадение, либо ничего. Модуль re вызывает исключение re.error, 
# если ошибка возникает при компиляции или использовании регулярного выражения.


import re
# compile()
# В Python есть возможность заранее скомпилировать регулярное выражение, а затем использовать его. Это особенно 
# полезно в тех случаях, когда регулярное выражение много используется в скрипте.
# Использование компилированного выражения может ускорить обработку, и, как правило, 
# такой вариант удобней использовать, так как в программе разделяется создание регулярного выражения и его использование. Кроме того, при использовании функции re.compile создается объект RegexObject, у которого есть несколько дополнительных возможностей, которых нет в объекте MatchObject.

# ---- метод match----
pattern = re.compile('for')  # создаём экземпляр класса от модуля re 
result = pattern.match('for')  # Output: <re.Match object; span=(0, 3), match='for'>
# match работает как == или in , если хоть какой-то символ не совпадает, выходит None, 
# он ищет только в начале строки, если искать в середине, то выходит ошибка 
print(result)

# ---- метод search----
# Функция search() будет искать шаблон регулярного выражения и возвращать первое вхождение. В отличие от Python match(), он проверяет все строки входной строки. 
# Функция Python search() возвращает объект соответствия, когда шаблон найден, и «ноль», если шаблон не найден.
string = 'look for the specific word for you can'
result = re.search('specific', string)  # Output: 
print(result)
print()
 


full = re.compile('look for the specific word for you can')
string = 'look for the specific word for you can'

# Обычный способ чтобы найти, находится ли строка в другой строке
# print("look" in string)  Output: True


# Scan through string looking for a match to the patterns,
# returning a Match object, or None if no match was found
print(re.search('specific', string))
a = re.search('specific', string)
print("group", a.group())
print(a.span())
print(a.start())  # первый индекс совпадения
print(a.end())    # последний индекс совпадения

a = pattern.search(string)
print(a.span())
print(a)

b = pattern.findall(string) # выводит все возникновение искаемой строки
print(b)
c = full.fullmatch(string) # проверяет равны ли строки между собой /вернет объект сопоставления, если  
                            # две строки полностью одинаковы
print(c)

# Использование re.findall()с группами соответствия — это мощный способ извлечения подстрок из вашего текста. 
# Но вы получаете только список строк , что означает, что вы потеряли позиции индекса, к которым у вас был доступ при использовании re.search().

# match()	Определить, соответствует ли RE началу строки.
# search()	Просканировать строку и найти любое место соответствия RE.
# findall()	Найти все подстроки соответствующие RE и вернуть их в виде списка.
# finditer()	Найти все подстроки соответствующие RE и вернуть их как итератор.
# group()	Возвращает строку, совпадающую с RE
# start()	Возвращает стартовую позицию соответствия
# end()	Возвращает конечную позицию соответствия
# span()	Возвращает кортеж, содержащий (начальные, конечные) позиции соответствия