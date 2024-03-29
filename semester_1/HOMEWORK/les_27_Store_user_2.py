USERS=[
    {   'name': 'Sabina',
        'email': 'sa@',
        'password': '123456',
        'purchases': [],
        'card': {'code': '1234567891234567', 'balance': 1000}
    }
]

PRODUCTS = {
    'pencils': 100, 
    'bag': 300, 
    'book': 50, 
    'vitamins': 150
}

class Store:
    purchases = []

    def __init__(self, name, email, password, card_code, card_balance): 
        self.name=name
        self.email=email
        self.password=password
        self.card_code=card_code
        self.card_balance=card_balance
        
    @classmethod
    def login(cls, email, password):
        if not (email and password):
            return "Empty values were given"
        for user in USERS:
            if user ['email'] == email and user ['password'] == password:
                return (cls, user ['name'], email, password, user ['card']['code'], user ['card']['balance'])
                # в этой строке создаём экземпляр класса
        return "Wrong email or password"

    @classmethod
    def register(cls, name, email, password, card_code, card_balance):
        """Регистрация и создание пользования.
        Полное описание из 120 и более символов.
        Args: 
            name(str): Имя пользователя
            email (str): email пользователя
            password (str): пароль 
            card_code (str):номер карты 
            card_balance(int): баланс карты

        Returns:
            Store class instance
        """
        # Есть ли данный пользователь в системе
        for user in USERS:  
            if user ['email'] == email or user ['password'] == password:
                return "Пользователь с такими данными уже есть"

        if not(name and email and password and card_code and card_balance):
            return "Empty values were given"
        if name.isalpha() and '@' in email and len(password) >=6 and len(card_code) == 16 and int(card_balance) >=0:
            USERS.append(
                {
                'name': name,
                'email': email,
                'password': password,
                'purchases': [],
                'card': {'code': card_code, 'balance': card_balance}
                }
            )
               # return Store (name, email, password, card_code, card_balance) 
            return cls(name, email, password, card_code, card_balance) 
            # в этой строке вызываем класс, возвращаем экземпляр класса. 
        else: 
            return "Wrong credentials"
    
    def purchase(self, product):
        if product not in PRODUCTS.keys():
            return "Not available" 
        if int(self.card_balance) <=0:
            return "Not enough money!"

        for key, val in PRODUCTS.items():
            if key == product and int(self.card_balance) - val >= 0: 
                self.card_balance = int (self.card_balance) - val
                self.purchases.append(product)
                for id, user in enumerate(USERS): 
                    if user ['email'] == self.email: 
                        USERS [id]['purchases'].append(product)
                PRODUCTS.pop(key)
                return f'\nSuccessfully bought {product} and added into purchases!\nBalance: {self.card_balance}\nYour purchases: {self.purchases}'  
                
        return f"{self.name} | {self.card_balance}: Not enough money."
                       
enter= input("Choose method, register or login:")
if enter == "login":
    user = Store.login(input("For signing in enter your email:"), input("Enter your password:"))
    print(user.purchase(input("What product do you want to buy?")))
    
elif enter == "register":
    user = Store.register(input("For the registration, please, enter your name:"), input ("e-mail:"), input("password:"),
           input("code_of_card:"), input("balance of your card:"))
    print(user.purchase(input("What product do you want to buy?")))
    # else: 
    #     print("Wrong email or password")
for user in USERS: 
    print(user)
# print("User's list:", USERS)
print(PRODUCTS)
