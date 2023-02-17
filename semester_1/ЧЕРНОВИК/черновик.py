USERS=[
        {
        'login_name': 'sabina'  ,
        'log_password' : 'Ss1@',
        'password_card': '1111' ,  
        'balance' : 1000000,
        }
    ]


class Atm: 
    service_charge=5
    cash_charge=3

    def __init__(self, login, log_in_password, card_password, balance):
        self.login = login
        self.log_in_password=log_in_password
        self.card_password = card_password
        self.balance = balance

    @classmethod
    def register(cls, login, log_in_password, card_password, balance):
        if login and log_in_password and card_password and balance:
            if log_in_password.istitle().isdigit() and "@" in log_in_password: 
                USERS.append(
                {
                    'login' : login, 
                    'log_in_password': log_in_password,
                    'card_password': card_password,
                    'balance': balance,
                }
            )
                print("Добро пожаловать " + login + "!")
                return cls(login, log_in_password, card_password, balance)
            else: 
                return ("Пароль для входа должен состоять хотя бы из одной заглавной, строчной буквы, цифры и '@'")

        if not (login and log_in_password and card_password and balance):
            return "Введите данные"
    
    def log_in(self, login, log_in_password, card_password, balance): 
        if not (login and log_in_password and card_password):
            return "Пожалуйста, проверьте правильность данных"
        for user in USERS(): 
            if user ['login_name']== login and user ['log_password'] == log_in_password and user['password_card'] == card_password and user['balance'] == True: 
                print("Добро пожаловать " + login + "!")
            return (user['login_name'], user['log_password'], user['password_card'], user['balance'])

    def deposit(self):
        deposit_card = input("На какую сумму хотите пополнить счёт? ")
        money = int(self.balance) + int(deposit_card)
        return f'\n{self.login.title()}, Вы пополнили счёт на: {str(deposit_card)}, Ваш баланс: {str(money)}'

    def get_cash(self):
        cash = input("Сколько Вы хотите снять? ")
        percent=int(cash) * self.service_charge/100
        money = int(self.balance) - int(cash) - percent
        return f'\n{self.login.title()}, Вы сняли {str(cash)}, Проценты за снятие денег: {str(percent)}, Ваш баланс {str(money)}' 

    def currency_exchange(self):
        exchange = input("Какую сумму Вы хотите обменять? ")
        percent_sum=int(exchange) * self.service_charge/100 
        percent_conversion= int(exchange) * self.cash_charge/100 
        money = int(self.balance) - int(exchange) - percent_sum - percent_conversion
        return f'\n{self.login.title()}, Вы обменяли: {str(exchange)}, \nПроценты с нац.валюты:  {str(percent_sum)}, \nПроценты с иностр.валюты:  {str(percent_conversion)}, \nВаш баланс:  {str(money)}' 

    def transfer(self): 
        transfer_card=input("На какую карту Вы хотите перевести деньги? 1. Humo / 2. Uzcard ")
        card_number=input("Введите номер карты: ")
        transfer_sum=input("Какую сумму хотите перевести? ")
        if transfer_card == "1":
            percent=int(transfer_sum) * 1.3/100 
            money=int(self.balance) - int(transfer_sum) - percent
            return f'Вы успешно перевели {str(transfer_sum)} сум на карту {str(card_number)}. Сумма списания с Вашей карты: {str(transfer_sum)} + {str(percent)}. Ваш баланс: {str(money)}' 
        if transfer_card == "2":
            percent=int(transfer_sum) * 1.4/100 
            money=int(self.balance) - int(transfer_sum) - percent
            return f'Вы успешно перевели {str(transfer_sum)} сум  на карту {str(card_number)}. Сумма списания с Вашей карты: {str(transfer_sum)} + {str(percent)}. Ваш баланс: {str(money)}'

enter=input("\nДля регистрации, введите 'R' / \n\nДля входа, введита 'E'" )
    
if enter == "R": 
    data = Atm.register(input("Введите логин для регистрации: "), input("Введите пароль для входа: (Пароль для входа должен состоять хотя бы из одной заглавной, строчной буквы, цифры и '@') "), input("Введите пароль карты: "), input("Введите баланс: ") )

if enter == "E":
    data = Atm.log_in(input("Введите логин: "), input("Введите пароль для входа: "), input("Введите пароль карты: "), input("Введите баланс карты: "))
  
# if enter !="R" or enter !="E":
#     print("Неправильный ввод, введите 'R' или 'E' ")
#     enter_active=True
#     while enter_active: 
#         enter == input("\nДля регистрации, введите 'R' / \nЕсли Вы зарегистрированный пользователь, для входа, введита 'E'" )
#         if enter == "R" or enter =="E": 
#             enter_active = False

choise = input("Выберите нужное меню: 1. 'Пополнение счёта', 2. 'Снятие наличных', 3. 'Обмен валюты': , 4. 'Перевод на карту': ")

if choise == "1":
    print(data.deposit())

if choise == "2":
    print(data.get_cash())

if choise == "3":
    print(data.currency_exchange())

if choise == "4": 
    print(data.transfer())

