#  Создать программу, которая проверяет, есть ли в словаре ключ "race" и "age", где значение ключа "age" должно быть 
# числом. Если проверка прошла, вывести на экран значение "race" и "age", если нет, вывести на экран строку human.
#
# #  1-method:====================================

d={
    'race': 'first', 
    'age': 18
}
if 'race' and 'age' in d:
    print(d.values())      # dict_values(['first', 18])
else: 
    print('Human')

# 2-method======================================
d={'race': 'First', 'age': 22}
if d.get('race' or 'age'):
    print(d.values())
else: 
    print('Human')
