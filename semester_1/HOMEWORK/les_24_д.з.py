# 1- задание: 
#  Создать класс с методами для умножения, возведения в степень, нахождения площади квадрата, круга, и треугольника  

class MatMethods: 

    def multiply(self, a, b):
        return a*b

    def exponentiation(self, a, b):
        return a**2, b**2
    
    def square_area(self,a):
        """Нахождение площади квадрата"""
        return a*a
    
    def circle_area_1(self, radius_of_the_circle):
        import math 
        """Нахождение площади круга по радиусу"""
        return (radius_of_the_circle**2)* math.pi
    
    def circle_area_2(self, diameter_of_the_circle):
        import math
        """Нахождение площади круга по диаметру"""
        return (diameter_of_the_circle**2)/4*math.pi

    def circle_area_3(self, length_of_the_circle):
        import math
        """Нахождение площади круга через длину окружности"""
        return (length_of_the_circle**2)/(4*math.pi)

    def triangle_area_1(self,base, height):
        """ Нахождение площади для любого треугольника: 
        1. Площадь треугольника через основание и высоту"""
        return (0.5*base*height)

    def triangle_area_2(self,length_a, length_b, angle):
        import math
        """ Нахождение площади для любого треугольника: 
        2. Площадь треугольника через две стороны и угол между ними S=a*b*sin(alpha*pi/180)/2 """
        return round(length_a * length_b * (angle * math.pi /180) /2)

    def triangle_area_3(self,a, b, c):
        import math
        """ Нахождение площади для любого треугольника: Формула Герона
        Площадь треугольника если известна длина трёх сторон"""
        p=(a+b+c)/2
        return math.sqrt(p*(p-a)*(p-b)*(p-c))


mat_methods=MatMethods()
print("Multiply:", mat_methods.multiply(5,2))
print("Exponentiation:", mat_methods.exponentiation(5,2))
print("Square_area:", mat_methods.square_area(2))

print("Find circle_area with radius of the circle:", mat_methods.circle_area_1(1.3))
print("Find circle_area with diameter of the circle:", mat_methods.circle_area_2(1.2))
print("Find circle_area with length of the circle:", mat_methods.circle_area_3(8))

print("Find triangle_area with base and height:", mat_methods.triangle_area_1(5,6))
print("Find triangle_area with a, b and angle:", mat_methods.triangle_area_2(4,5,30))
print("Find triangle_area with a, b, c (Heron's formula):", mat_methods.triangle_area_3(3,4,5))

# ============================================================================================================
# 2-задание: Создать класс, который описывает игрового персонажа с атрибутами (health, mana, damage, type, skill) и 
# методами attack, heal, level_up от которого наследуются 3 класса Archer, Paladin, Wizard. На свою фантазию можете
# расширить функциональность 

# class GameCharacter:
    
#     def __init__(self,health, mana, damage, type, skill):
#         self.health=health
#         self.mana=mana
#         self.damage=damage
#         self.type=type
#         self.skill="flying", "learning magical creatures", "Potions"
    
#     def attack(self):

#     def heal():

#     def level_up():

# class Archer(GameCharacter):
#     pass

# class Paladin(GameCharacter):
#     pass

# class Wizard(GameCharacter):
#     pass 

# game_character=GameCharacter()

# print(archer.)

# paladin=Paladin()
# print(paladin.)

# wizard=Wizard()
# print(wizard.)