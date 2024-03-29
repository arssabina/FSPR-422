import csv

USERS = [
    {
        'name': 'Behruz',
        'password': '234fjfdsd',
        'email': 'behruz@gmail.com',
        'purchases': [],
        'card_code': '3647583465734283', 
        'card_balance': 1000
    }
]
# PRODUCTS = {
#     'key': 3,
#     'wear': 200,
# # }
PRODUCTS = [
    {
        "product_name": "sweater",
        "count": 10,
        "price": 100,
        "type": "black",
    },
]


class StoreOwner:
    pass


class Store:
    purchases = []

    def __init__(self, name, email, password, card_code, card_balance):
        self.name = name
        self.email = email
        self.password = password
        self.card_code = card_code
        self.card_balance = card_balance

    @classmethod
    def login(cls, email, password):
        if not (email and password):
            return 'Empty values were given.'
        for user in USERS:
            if user['email'] == email and user['password'] == password:
                return cls(user['name'], email, password, user['card']['code'], user['card']['balance'])
        return 'Wrong email or password'

    @classmethod
    def register(cls, name, email, password, card_code, card_balance):
       users_data = []
       users_keys = ""

       with open ("users.csv") as users:
        users_reader = csv.DictReader(users, delimiter = ";")
        users_keys = users_reader.fieldnames
        for row in users_reader: 
            users_data.append(
                {
                    'id': row ['id'],
                    'name': row ['name'],
                    'password': row ['password'],
                    'email': row ['email'],
                    'purchases': row ['purchases'],
                    'card_code': row ['card_code'],
                    'card_balance': row ['card_balance'],


                }
            )
        # Есть ли данный пользователь в системе
        for user in users_data:
            if user['email'] == email and user['password'] == password:
                return "Пользователь с такими данными уже есть."

        if not (name and email and password and card_code and card_balance):
            return 'Empty values were given.'
        if (
            name.isalpha() 
            and '@' in email 
            and len(password) >= 6 
            and len(card_code) == 16 
            and card_balance >= 0
        ):
            with open('users.csv', 'a', newline = '') as users_file: 
                users_writer = csv.DictWriter(users_file, fieldnames=users_keys, delimiter=";")
                users_writer.writerow({                    
                        "id": int(users_data[-1]["id"]) + 1, 
                        'name': name,
                        'passwrod': password,
                        'email': email,
                        'purchase': [],
                        'card_code': card_code,
                        'card_balance': card_balance,
                    }
                )
            return cls(name, email, password, card_code, card_balance)
        else:
            return 'Wrong credentials!'

    def purchase(self, product):
        if product not in PRODUCTS.keys():
            return 'Not available!'
        if self.card_balance <= 0:
            return "Not enough money!"

        for key, val in PRODUCTS.items():
            if key == product and self.card_balance - val >= 0:
                self.card_balance -= val
                self.purchases.append(product)
                for id, user in enumerate(USERS):
                    if user["email"] == self.email:
                        USERS[id]['purchases'].append(product)
                PRODUCTS.pop(key)
                return f'\nSuccesfully bought {product} and added into purchases!\nBalance: {self.card_balance}\nYour purchases: {self.purchases}'

        return f'{self.name} | {self.card_balance}: Not enough money.'
    
user_1 = Store.register("Sabina", "sabina@mail.ru", "sabina1212", "123456789123456", 1200)