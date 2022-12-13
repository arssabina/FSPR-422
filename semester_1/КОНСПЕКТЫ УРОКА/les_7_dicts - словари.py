# Итерируемые - iterable. Исчисляемый. Это те переменные, которые хранят больше одного значения
# Индексы

names=[1,3,4,5]  #3
print(type(names), names[3])
names=()
print(type(names))

# Dictionary - словарь
# Ключом словаря могут быть только не изменяемые типы переменных

user_data={
  "ключ": "значение", 
    1: None,
    2: 21,
    3: 6.7,
    4: [2,3,4],
    5: (1,2,3),
    6: {"key": "Другой словарь"}
    # [1]: 23, # error
    # (2,3, [2,3]): "Error", # кортеж можно использовать как ключ, но не реком-ся
}

#40-50  kljfd;lkjgldfk.jnb 
print(type(user_data), user_data, user_data ["ключ"], sep="\n")

# переписать код и вывести на экран все значения словаря
print(type(user_data), user_data[1], user_data [2], user_data[3], user_data [4], user_data[5], user_data [6], sep="\n")


user_data = {
    "username": "Gobby", 
    "password": "546546hd",
    "age": 18, # hash 46546ckhbdiuygdsfu
    "age": 22, # hash oijdfilugkhjeriu5
}

print(user_data["age"])



user_data["username"] = "Alabasta"
print(user_data.keys(), user_data.values(), user_data.items(), sep="\n")
# для вывода ключей              значений    ключа-значения

# dict_keys(['username', 'password', 'age'])
# dict_values(['Alabasta', '546546hd', 22])
# dict_items([('username', 'Alabasta'), ('password', '546546hd'), ('age', 22)])


user_list = list (user_data.values()) # 
print(user_list)

print("get", user_data.get("age"), user_data.get("unexisting"))



user_data_2 = {
    "username": "Gobby", 
    "password": "546546hd" , 
    "age": 18, 
    "age": 22, 
}

user_data = [
    {
    "username": "Gobby", 
    "password": "546546hd" ,
    "age": 18,
}, 
{   
    "username": "Apoy", 
    "password": "546546dfdfghd" ,
    "age": 14,
},
]
print(user_data[0]["username"], user_data[0] ["age"] )


a={2,3,4, "hello", 2, 4}
print(a)
a={} # set|dict
print(type(a))
a=set()
print(type(a))

b=[1,2,3,4,5,6,1,2,3,4, "AA", "BB", "AA"]
print(b, set(b), sep="\n")

print(b, list(set(b)), sep="\n")

