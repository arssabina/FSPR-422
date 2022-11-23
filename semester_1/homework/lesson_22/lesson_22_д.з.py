# How to find next palindrome number   Мой вариант решения 
# https://www.codewars.com/kata/56a6ce697c05fb4667000029/train/python
# def palindrom(n):
#     n=n+1
#     while True:
#         n=str(n)        # переводим номер в строку 
#         number=n[::-1]  # переворачиваем номер 
#         if n==number:       
#             print(int(n))
#             break
#         else: 
#             n=int(n)
#             n=n+1

# palindrom(33)

# ============================================================
# https://www.codewars.com/kata/5174a4c0f2769dd8b1000003/solutions/python
# Sort numbers: Finish the solution so that it sorts the passed in array of numbers. 
# If the function passes in an empty array or null/nil value then it should return an empty array.

# def solution(nums):
#     if nums:
#         print(sorted(nums))
#     else:
#         print([])

# solution([1,2,5,8,99])

# =============================================================
# 2-задание: 
# Cоздать класс, который описывает машину с атрибутами: модель, цвет, цена, страна, двигатель ...
# и с методами: ускорение за секунду, расход топлива за прохожденный путь 
# (если топливо закончится, вывести на экран пройденный путь и оставшийся)

class Car():
    норма_расхода=float(7.7)       # 7,7 л/100 км
    было_до_заливки=10   # л в бензобаке
    залили_топлива=30       # л
    
    """Description of the car"""
    def __init__(self, model, color, price, manufacturer_country, engine):
        self.model=model
        self.color=color
        self.price=price
        self.manufacturer_country=manufacturer_country
        self.engine=engine

    def function(self, расход_топлива):
        self.остаток_топлива=self.было_до_заливки+self.залили_топлива-расход_топлива
        self.пройденный_путь =расход_топлива/self.норма_расхода * 10

        if self.остаток_топлива <=0:
            print("Бензин на исходе! Пройденный путь: ", self.пройденный_путь) 
    
car=Car("Mercedes-Benz GLC 300 4 MATIC", "white", "61 400 EUR", "Germany", "Petrol engine")
car_1=Car("LAND CRUISER 300", "white", "135 000 $", "Japan", "Petrol engine")
print("\n""Model: " + car.model, "color: " + car.color, "Price: " + car.price, "Manufacturer country: " +  
car.manufacturer_country, "Engine: " + car.engine, sep="\n")
print("\n\n""Model: " + car_1.model, "color: " + car_1.color, "Price: " + car_1.price, "Manufacturer country: " + 
car_1.manufacturer_country, "Engine: " + car_1.engine, sep="\n")

car.function(40.0)
print("\n""Остаток топливa: " + str(car.остаток_топлива) + " л.")
print("\n""Пройденный путь: " + str(car.пройденный_путь) + " км.")


# 3-задание: Создать класс описывающий человека с методами которые описывают вас (что умеете) 
class Person:
    name="Sabina"
        
    def __init__(self, eyes, hair_color, height):
        self.eyes=eyes
        self.hair_color=hair_color
        self.height=height

    def cooking(self,cuisine, cakes, other_dishes):
        self.cuisine=cuisine
        self.cakes=cakes
        self.other_dishes=other_dishes
        
person=Person("brown", "black", 1.72)

print("My name is " + person.name + ". " + "My eyes are " + person.eyes + "," + " hair is " + 
person.hair_color  + "," + " my height is " + str(person.height) + ".")
person.cooking("Uygur national dishes", "great cakes","salads, cuisine dishes")
print("I like cooking. I can cook " + person.cuisine +", " + person.cakes + ", " +  person.other_dishes)

    










