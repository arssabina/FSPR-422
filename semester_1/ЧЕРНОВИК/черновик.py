# # Дз 
# # """"
# # 1. Создать класс с атрибутами: name, email, password, purchases (список), card 
# # методами: 
# # - purchase - метод для покупки товаров. 
# #     Для покупки вам нужно узнать, какой товар хочет купить человек и есть у него достаточно денег для этого. 
# #     Если условия верны, то человек покупает товар и с его счета снимаются деньги 
# #     Если товара нет в списке товаров, вывести сообщение что товара нет, если не достаточно денег,  
# #     то вывести сообщение что не достаточно средств. 
 
# # - register - создать нового пользователя и включить его в список пользователей если: 
# #     name - должен содержать только буквы 
# #     email - должен содержать @ 
# #     password - миинмальная длинна 6 
# #     card - длина ключа code была равна 16 
 
# #     Если все условия прошли, то создать пользователя с атрибутами и записать его данные в переменную USERS. 
 
# # - login - вход в систему, если пользователь уже есть. При этом пользователь должен иметь все свои данные:  
# #     покупки, список купленных товаров и т.д 
# #     Для логина вам нужно узнать, есть ли такой пользователь в системе или нет. Если его нет, то сказать что нужно пройти регистрацию. 
# #     Если есть, то создать все атрибуты класса из имеющихся данных. 
 
# # - add_product - добавить купленный товар в атрибут purchases."""

# class Store:
#     USERS={}
#     user_data=[]
#     purchases=[]
#     products={'pencils': 100, 'bag': 300, 'book': 50, 'vitamins': 150}
#     account_balance=[]
    
#     def __init__(self, name, email, password, code_of_card): 
#         """Ввод данных нового пользователя"""
#         self.name=name
#         self.email=email
#         self.password=password
#         self.code_of_card=code_of_card

#     def __repr__(self):
#         """Проверка данных нового пользователя"""
#         if self.name.isalpha() == True and "@" in self.email and len(self.password) == 6 and len(self.code_of_card) ==1:
#             self.USERS={"user's name": self.name, 'e-mail' : self.email, 'password' : self.password, 'code_of_card': self.code_of_card}
#             print(self.USERS)
#             return f"Registration is successful"
#         else: 
#             return f"Incorrect information"

#     def login_user(self, login):
#         """Ввод данных зарегистрированного пользователя"""
#         self.login=login
            
#         if self.login in self.USERS.values(): 
#             self.user_data=self.USERS.copy()
#             print("You signed in, welcome!")
#             print(self.user_data)
#         else: 
#             print("You are not registered. Please register on the site!")
    
#     def purchase(self, wish_product, enough_money):
#         self.wish_product=wish_product
#         self.enough_money=enough_money  

#         """Покупка товара и списание средств со счету"""
#         if self.wish_product in self.products.keys() and int(self.enough_money) >= int(self.products[self.wish_product]):
#             self.account_balance=int(self.enough_money) - int(self.products[self.wish_product])            
#             self.purchases.append(self.wish_product)
#             print("Successful purchase!\nPurchased_product:", self.wish_product, ",", "price:", 
#                       self.products[self.wish_product], ",", "your current account_balance:", self.account_balance)
        
#         """Недостаточно средств на счету"""
#         if int(self.enough_money) < int(self.products[self.wish_product]):
#             print("Sorry, you don't have enough money")

#         if self.wish_product not in self.products.keys():
#             print("Sorry, we don't have this product")
    
                  
# store_user=Store(input("For the registration, please, enter your name:"), input ("e-mail:"), input("password:"),
#            input("code_of_card:"))
# print(store_user)
# reg_user=store_user.login_user(input("For signing in enter your login:")) 
# puchase=store_user.purchase(input("What do you want to buy?"), input("How much money do you have?"))
# print("Your purchased products:", store_user.purchases)



def doors(n):
    door_status = []
    for a in range(0, n):
        door_status.append(False)
    for a in range(0,n):
        for b in range(a,n,a+1):
            door_status[b] = not door_status[b]
    result = 0

    for a in range(0,n):
        if door_status[a] == True: result += 1
    return result

print(doors(10))