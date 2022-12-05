# Дз 
# """"
# 1. Создать класс с атрибутами: name, email, password, purchases (список), card 
# методами: 
# - purchase - метод для покупки товаров. 
#     Для покупки вам нужно узнать, какой товар хочет купить человек и есть у него достаточно денег для этого. 
#     Если условия верны, то человек покупает товар и с его счета снимаются деньги 
#     Если товара нет в списке товаров, вывести сообщение что товара нет, если не достаточно денег,  
#     то вывести сообщение что не достаточно средств. 
 
# - register - создать нового пользователя и включить его в список пользователей если: 
#     name - должен содержать только буквы 
#     email - должен содержать @ 
#     password - миинмальная длинна 6 
#     card - длина ключа code была равна 16 
 
#     Если все условия прошли, то создать пользователя с атрибутами и записать его данные в переменную USERS. 
 
# - login - вход в систему, если пользователь уже есть. При этом пользователь должен иметь все свои данные:  
#     покупки, список купленных товаров и т.д 
#     Для логина вам нужно узнать, есть ли такой пользователь в системе или нет. Если его нет, то сказать что нужно пройти регистрацию. 
#     Если есть, то создать все атрибуты класса из имеющихся данных. 
 
# - add_product - добавить купленный товар в атрибут purchases."""

USERS=[
    {   'name': 'Sabina',
        'email': 'sa@',
        'password': '123456',
        'purchases': [],
        'card_code': '1234567891234567',
        'card_balance': 1000
    }
]


class Store:
    purchases = []

    def __init__(self, name, email, password, card_code, card_balance): 
        self.name=name
        self.email=email
        self.password=password
        self.card_code=card_code
        self.card_balance=card_balance

    @classmethod
    def register(cls, name, email, password, card_code, card_balance):
        for user in USERS:  
            """для проверки есть ли такой пользователь или нет. если такой пароль и email уже существует, 
            вывеcти сообщение что есть такой пользователь"""
            if user ["email"] == email or user ["password"] == password:
                return "Wrong email or password"
            else: 
                break

        if not(name and email and password and card_code and card_balance):
            return "Empty values were given"

        if name.isalpha() and '@' in email and len(password) >=6 and len(card_code) == 16:
            USERS.append(
                {
                'name': name,
                'email': email,
                'password': password,
                'purchases': [],
                'card': card_code,
                'card balance': card_balance
                }
            )
            # return Store (name, email, password, card_code, card_balance) 
            return cls(name, email, password, card_code, card_balance) # в этой строке создаём экземпляр класса, 
            # в этой стркое вызываем класс, возвращаем экземпляр класса. 
        else: 
            return "Wrong credentials"
       
    @classmethod
    def login(cls, email, password):
        for user_1 in USERS:
            if user_1 ["email"] == email and user_1 ["password"] == password:
                return (cls, email, password)  # в этой строке создаём экземпляр класса
            else: 
                return "You are not registered. Please register on the site!"

enter_method= input("Choose method, register or login:")
if enter_method == "register":
    user_1 = Store.register(input("For the registration, please, enter your name:"), input ("e-mail:"), input("password:"),
           input("code_of_card:"), input("balance of your card"))
elif enter_method == "login":
    user_1 = Store.login(input("For signing in enter your email:"), input("Enter your password:"))
print(user_1)
# print(USERS)
