# Дз 
""""
1. Создать класс с атрибутами: name, email, password, purchases (список), card 
методами: 
- purchase - метод для покупки товаров. 
    Для покупки вам нужно узнать, какой товар хочет купить человек и есть у него достаточно денег для этого. 
    Если условия верны, то человек покупает товар и с его счета снимаются деньги 
    Если товара нет в списке товаров, вывести сообщение что товара нет, если не достаточно денег,  
    то вывести сообщение что не достаточно средств. 
 
- register - создать нового пользователя и включить его в список пользователей если: 
    name - должен содержать только буквы 
    email - должен содержать @ 
    password - миинмальная длинна 6 
    card - длина ключа code была равна 16 
 
    Если все условия прошли, то создать пользователя с атрибутами и записать его данные в переменную USERS. 
 
- login - вход в систему, если пользователь уже есть. При этом пользователь должен иметь все свои данные:  
    покупки, список купленных товаров и т.д 
    Для логина вам нужно узнать, есть ли такой пользователь в системе или нет. Если его нет, то сказать что нужно пройти регистрацию. 
    Если есть, то создать все атрибуты класса из имеющихся данных. 
 
- add_product - добавить купленный товар в атрибут purchases."""
class Store:
    new_user_info={}
    passwords=[]
 
    def __init__(self, name, email, password, code_of_card): 
        self.name=name
        self.email=email
        self.password=password
        self.code_of_card=code_of_card

    def __repr__(self):
        if self.name.isalpha() == True and "@" in self.email and len(self.password) == 6 and len(self.code_of_card) ==1:
            self.new_user_info={'name': self.name, 'e-mail' : self.email, 'password' : self.password,
            'code_of_card': self.code_of_card}
            print(self.new_user_info)
            return f"Registration is successful"
        else: 
            return f"Incorrect information"
   
       
user=Store(input("Enter your name:"), input ("e-mail:"), input("password:"), input("code_of_card:"))
print(user)
