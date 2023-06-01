# username=input("Enter your username:")
# password=input("Enter your password:")
# USERS = {
#     'username': 'Sabina',
#     'password': 123456,

# }
# usernames=[]

# def register(username, password):
#     if username in usernames: 
#         print("Пользователь с таким именем уже существует")
#         return
#     if len(password) < 6:
#         print('Длина пароля меньше 6')
#         return
#     else: 
#         user = {
#             'username': username,
#             'password': password,
#         }
#         USERS.append(user)
#         usernames.append()
#         return USERS
# print(USERS)
# def authorize(func):
#     def  wrapper(*args, **kwargs):
#         if register(username, password): 
#             func(*args, **kwargs)
#     return wrapper

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