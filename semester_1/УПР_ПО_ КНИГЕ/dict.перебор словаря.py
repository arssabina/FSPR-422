"""
6-3. Глоссарий: словари Python могут использоваться для моделирования «настоящего» 
словаря (чтобы не создавать путаницы, назовем его «глоссарием»).
• Вспомните пять терминов из области программирования, которые вы узнали в предыдущих главах. Используйте эти 
лова как ключи глоссария, а их определения — как 
значения.
• Выведите каждое слово и его определение в аккуратно отформатированном виде.
Например, вы можете вывести слово, затем двоеточие и определение; или же слово 
в одной строке, а его определение — с отступом в следующей строке. Используйте 
символ новой строки (\n) для вставки пустых строк между парами «слово-определение» в выходных данных."""

python_dict={
    "set"  : "множество",
    "dict" : "словарь",
    "tuple" : "кортеж",
    "list" : "список",
    "str" : "строка",
}
for key, value in python_dict.items():
    print(key + " is" + " " + value + "." )

"""
6-5. Реки: создайте словарь с тремя большими реками и странами, по которым протекает 
каждая река. Одна из возможных пар «ключ—значение» — ‘nile’: ‘egypt’.
• Используйте цикл для вывода сообщения с упоминанием реки и страны — например, 
«The Nile runs through Egypt.»
• Используйте цикл для вывода названия каждой реки, включенной в словарь.
• Используйте цикл для вывода названия каждой страны, включенной в словарь."""

rivers={
    "nile" : "egypt",
    "amazon" : "south america", 
    "mississippi" : "USA", 
    "huang he" : "china",
    "volga" : "Russia", 
}

for key, value in rivers.items():
    print(key.title() + " runs through" + " " + value.title() + ".")

print("\nRivers:")
for key in rivers.keys():
    print (key.title())

print("\nCountries:")
for country in rivers.values():
    print(country.title())

"""
6-6. Опрос: Возьмите за основу код favorite_languages.py (с. 106).
• Создайте список людей, которые должны участвовать в опросе по поводу любимого языка программирования. 
Включите некоторые имена, которые уже присутствуют в списке, и некоторые имена, которых в списке еще нет.
• Переберите список людей, которые должны участвовать в опросе. Если они уже прошли опрос, выведите сообщение
с благодарностью за участие. Если они еще не проходили опрос, выведите сообщение с предложением принять участие."""

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

persons_for_poll=["sarah", "farina", "tamina", "hanifa", "edward"]
for name in persons_for_poll:
    if name in favorite_languages.keys():
        print(name.title() +"," + " thank you for taking our poll!")
    else: 
        print(name.title() + "," + " please take our poll!")  

"""
6-7. People: Start with the program you wrote for Exercise 6-1 (page 102).
Make two new dictionaries representing different people, and store all three 
dictionaries in a list called people. Loop through your list of people. As you 
loop through the list, print everything you know about each person"""

kid_1={
    "farina" : "first", 
    "year of birth": 2011,
    "date of birth": "15 february",
    }
kid_2={
    "tamina" : "second", 
    "year of birth": 2016,
    "date of birth": "5 july",
    }
kid_3={
    "hanifa" : "third", 
    "year of birth": 2020,
    "date of birth": "18 april",
    }
my_kids=[kid_1, kid_2, kid_3]
for kid in my_kids:
    print(kid)
"""
6-8. Pets: Make several dictionaries, where the name of each dictionary is the 
name of a pet. In each dictionary, include the kind of animal and the owner’s 
name. Store these dictionaries in a list called pets. Next, loop through your list 
and as you do print everything you know about each pet"""
pussy={
    "cat" : "Asmira",
    }
doggy={
    "puppy" : "Farina",
    }
cute={
    "hedge" : "Tamina",
    }
pets=[pussy, doggy, cute]
for pet in pets: 
    print(pet)

"""
6-9. Favorite Places: Make a dictionary called favorite_places. Think of three
names to use as keys in the dictionary, and store one to three favorite places
for each person. To make this exercise a bit more interesting, ask some friends
to name a few of their favorite places. Loop through the dictionary, and print
each person’s name and their favorite place"""

favorite_places={
    "Mom": ["istanbul", "miami", "sochi"], 
    "Dad" : ["antalya", 'orlando', 'new york'], 
    "Samir" : ["stockholm", 'paris', 'oslo'], 
    'Bohir' : ['istanbul', 'beijing'],
}
for key, value in favorite_places.items():
    print("\n" + key.title() + "'s favourite places are: ")
    for place in value: # перебираем места,  которые сохранились в переменной value
        print("\t" + place.title())
        # Output: Mom's favourite places are:
            #       Istanbul
            #       Miami
            #       Sochi



"""
6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 102) so 
each person can have more than one favorite number. Then print each person’s 
name along with their favorite numbers"""
favorite_numbers={
    'farina': [5, 15, 7],
    'tamina': [5, 10],
    'hanifa': [1,18,4], 
}
for name, number in favorite_numbers.items():
    print("\n" + name.title() + "'s favourite numbers are:")
    for num in number:
        print("\t" + str(num))

"""
6-11. Cities: Make a dictionary called cities. Use the names of three cities as 
keys in your dictionary. Create a dictionary of information about each city and 
include the country that the city is in, its approximate population, and one fact 
about that city. The keys for each city’s dictionary should be something like 
country, population, and fact. Print the name of each city and all of the information you have stored about it"""

cities={
    'miami': {
        'country':'USA', 
        'population' : 439890, 
        'fact': 'Miami has the largest cruise ship port in the world',

    },
    'istanbul': {
        'country':'Turkey', 
        'population' : 15636000 , 
        'fact': 'Throughout most of its long history, Istanbul was known as Constantinople',
    },
    'antalya': {
        'country':'Turkey', 
        'population': 1203994, 
        'fact': 'Antalya is a large coastal city in Turkey',
    },
}

for city_name, city_info in cities.items():
    print("\nCity: " + city_name.title())
    for info in city_info.items():
        print(info)