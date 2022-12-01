class Father:
    house=True
    cooked_food=""

    def __init__(self, name, job, hobby, bank_account):
        self.name = name 
        self.job = job
        self.hobby = hobby
        self.bank_account = bank_account

    def spend(self, amount):
        self.bank_account -=amount

    def  income(self, amount):
        self.bank_account += amount


    def cook(self, products):
        if "carrot" in products and "rice" in products:
            self.cooked_food= "Father's plov"
        else: 
            print("We can't cook plov")


class Mother:
    cooked_food=""

    def cook(self, products):
        if "carrot" in products and "meat" in products and "rice" in products:
            self.cooked_food= "plov"
        else: 
            print("We can't cook plov")


class Child(Father, Mother):

    def __init__(self, name, job, hobby, bank_account, age):
        super().__init__(name, job, hobby, bank_account)  # расширяем класс Child используя импортирование методы класса Father,
        # мы импортируем чужой метод себе локально
        """мы должны писать все аргументы которые есть в отцовском классеб меньше или больше нельзя, выдаст ошибку"""
        self.age = age

    def cook(self, products):
        super().cook(products)
        if "масло" in products and "баклажаны" in products and "помидоры" in products: 
            self.cooked_food = "жареный баклажан"


# class ChildTwo(Father, Mother):
#     pass

child=Child("Sabina", "IT", "cooking", 100000, 36)
print(child.name, child.bank_account, child.hobby, child.age)

child.spend(300)
print(child.bank_account)

child.income(800)
print(child.bank_account)

child.cook(["carrot", "meat", "rice"])
print(child.cooked_food)

child.cook(["масло", "баклажаны", "помидоры"])
print(child.cooked_food)

child.cook(["carrot", "rice"])
print(child.cooked_food)






# ==================================================================================

# Создать метод который создает атрибут date_of_birth используя модуль datetime
import datetime 
date_of_birth = datetime.datetime(1986, 2, 12)                  #Задание даты
print("My date of birth:", date_of_birth)                       #Вывод даты на экран



import datetime 
date= datetime.datetime.now()                  #Задание даты
print(date)                                   