class Atm: 
    service_charge=5
    cash_charge=3

    def __init__(self, login, password, balance):
        self.login = login
        self.password = password
        self.balance = balance

    @classmethod
    def register(cls, login, password):
        login = input("Для регистрации введите логин: ")
        password = input("Придумайте пароль: ")

    def deposit(self):
        deposit_card = input("На какую сумму хотите пополнить счёт? ")
        money = int(self.balance) + int(deposit_card)
        return "\nВы пополнили счёт на: " + str(deposit_card), "Ваш баланс: " + str(money)

    def get_cash(self):
        cash = input("Сколько Вы хотите снять? ")
        percent=int(cash) * self.service_charge/100
        money = int(self.balance) - int(cash) - percent
        return "\nВы сняли " + str(cash), "Ваш баланс " + str(money), "Проценты за снятие денег: " + percent

    def currency_exchange(self):
        exchange = input("Какую сумму Вы хотите обменять? ")
        percent=int(exchange) * self.service_charge/100 + int(exchange) * self.cash_charge/100 
        money = int(self.balance) - int(exchange) - percent
        return "\nВы обменяли: " + str(exchange), "Ваш баланс: " + str(money), "Проценты за обмен валюты: " + str(percent)

data=Atm("sabina", 1212, input("Введите баланс: ") )
check_login = input("Введите логин: ")
check_password = input("Введите пароль: ")
enter = input("Выберите нужное меню: 1. 'Пополнение счёта', 2. 'Снятие наличных', 3. 'Обмен валюты': ")



if enter == "1":
    print(data.deposit())

if enter == "2":
    print(data.get_cash())

if enter == "3":
    print(data.currency_exchange())

