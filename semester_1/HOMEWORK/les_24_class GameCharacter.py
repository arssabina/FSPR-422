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

# # ============================================================================================================
# 2-задание: Создать класс, который описывает игрового персонажа с атрибутами (health, mana, damage, type, skill) и 
# методами attack, heal, level_up от которого наследуются 3 класса Archer, Paladin, Wizard. На свою фантазию можете
# расширить функциональность 
# 
class GameCharacter:
    experience = 0
    lvl=1

    def __init__(self,health, mana, damage, type, skills):
        self.health=health
        self.mana=mana
        self.damage=damage
        self.type=type
        self.skills=skills  # навыки будут выводиться в списке
    
    def attack(self, enemy_health):
        return enemy_health-self.damage


    def heal(self):
        if "heal" in self.skills:
            self.health +=10
    
    def kill_enemy(self, enemy_lvl):
        if enemy_lvl==1:
            self.experience +=5
            self.level_up()
            print(f"You lkeveled up. Your current level is {self.lvl}")

    def level_up(self):
        """максимальный уровень - 5 """
        if  10 <= self.experience <=20:
            self.lvl +=1
        elif 21 <= self.experience <=30:
            self.lvl +=1
        elif 31 <= self.experience <=40:
            self.lvl +=1
        elif 41 <= self.experience <=50:
            self.lvl +=1
        elif 51 <= self.experience:
            self.lvl +=1

class Archer(GameCharacter):
    pass

class Paladin(GameCharacter):
    pass

class Wizard(GameCharacter):
    pass 


player_1=GameCharacter(15,50,15,"base", ["heal"])
player_2=GameCharacter(15,50,15,"base", ["heal"])


# Второй игрок теряет жизнь
print(player_2.health)
player_2.health=player_2.health-player_1.attack()
print(player_2.health)


# Первый игрок теряет жизнь
print(player_1.health)
player_1.health=player_1.health-player_2.attack()
print("Player_1 health:", player_1.health)

player_1.heal()
player_2.heal()
print(player_1.health)
print(player_2.health)


